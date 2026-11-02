"""C ve C# kodu derleyip çalıştıran çok katmanlı motor (yalnızca tests/verify_content.py kullanır; uygulamada kod çalıştırma yok).

Katman 1 — Yerel derleyici: gcc/clang (C) veya mcs/csc + mono (C#) kuruluysa geçici bir dizinde
           derler ve 5 sn zaman aşımıyla çalıştırır. Streamlit Cloud'da packages.txt bunları kurar.
Katman 2 — Piston API (https://emkc.org/api/v2/piston/execute). Genel sunucu 15.02.2026'dan beri
           whitelist'e kapalı olduğundan PISTON_URL / PISTON_TOKEN ortam değişkenleriyle kendi
           sunucunuzu veya token'ınızı verebilirsiniz; erişim reddedilirse otomatik olarak sonraki
           katmana geçilir.
Katman 3 — Wandbox API (https://wandbox.org), ücretsiz ve anahtarsız son yedek.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, field

import requests

RUN_TIMEOUT = 5
COMPILE_TIMEOUT = 20
MAX_OUTPUT = 64_000
HTTP_TIMEOUT = 40

PISTON_DEFAULT_URL = "https://emkc.org/api/v2/piston/execute"
WANDBOX_URL = "https://wandbox.org/api/compile.json"

LANGS = {
    "c": {"label": "C", "file": "main.c", "piston": "c", "wandbox": ["gcc-13.2.0-c", "gcc-head-c", "gcc-12.3.0-c"]},
    "csharp": {"label": "C#", "file": "Program.cs", "piston": "csharp", "wandbox": ["mono-6.12.0.199", "mono-5.20.1.34"]},
}

ENGINE_LABELS = {
    "auto": "Otomatik (Yerel → Piston → Wandbox)",
    "local": "Yerel derleyici",
    "piston": "Piston API",
    "wandbox": "Wandbox API",
}

_C_DIAG = re.compile(r"^[^\n:]*?:(\d+):(\d+):\s*(fatal error|error|warning|note):\s*(.*)$", re.M)
_CS_DIAG = re.compile(r"\((\d+),(\d+)\):\s*(error|warning)\s+(CS\d+):\s*(.*)$", re.M)


@dataclass
class RunResult:
    ok: bool                      # program derlendi ve 0 koduyla bitti
    stage: str                    # "run" | "compile" | "timeout" | "unavailable"
    stdout: str = ""
    stderr: str = ""
    compile_output: str = ""      # derleyici mesajları (uyarı/hata)
    exit_code: int | None = None
    engine: str = ""
    elapsed: float = 0.0
    diagnostics: list = field(default_factory=list)
    notes: list = field(default_factory=list)  # denenen katmanlar / geçiş nedenleri


class EngineUnavailable(Exception):
    """Bu katman kullanılamıyor; bir sonrakine geçilmeli."""


def _clip(text: str) -> str:
    text = text or ""
    if len(text) > MAX_OUTPUT:
        return text[:MAX_OUTPUT] + f"\n… [çıktı {MAX_OUTPUT} karakterde kesildi]"
    return text


def _normalize_stdin(stdin: str) -> str:
    stdin = stdin or ""
    if stdin and not stdin.endswith("\n"):
        stdin += "\n"
    return stdin


def parse_diagnostics(lang: str, text: str) -> list[dict]:
    """Derleyici çıktısından satır numaralı hata/uyarı listesi çıkarır."""
    out = []
    if not text:
        return out
    if lang == "c":
        for m in _C_DIAG.finditer(text):
            sev = "error" if "error" in m.group(3) else m.group(3)
            if sev == "note":
                continue
            out.append({"line": int(m.group(1)), "col": int(m.group(2)), "severity": sev, "code": "", "message": m.group(4).strip()})
        # Bağlayıcı (ld) hataları satır numarası taşımaz: "main.c:(.text+0xf): undefined reference to `topla'"
        for m in re.finditer(r"(undefined reference to .+|multiple definition of .+)", text):
            out.append({"line": 0, "col": 0, "severity": "error", "code": "ld", "message": m.group(1).strip()})
    else:
        for m in _CS_DIAG.finditer(text):
            out.append({"line": int(m.group(1)), "col": int(m.group(2)), "severity": m.group(3), "code": m.group(4), "message": m.group(5).strip()})
    return out


def _clean_paths(text: str, workdir: str, filename: str) -> str:
    if not text:
        return text
    text = text.replace(os.path.join(workdir, filename), filename).replace(workdir + os.sep, "")
    return re.sub(r"/piston/jobs/[\w-]+/", "", text)


# ───────────────────────────── Katman 1: yerel ─────────────────────────────

def local_toolchain(lang: str) -> dict | None:
    """Kurulu yerel derleyiciyi bulur; yoksa None."""
    if lang == "c":
        for cc in ("gcc", "cc", "clang"):
            path = shutil.which(cc)
            if path:
                return {"compiler": path, "name": cc}
        return None
    mono = shutil.which("mono")
    for csc in ("mcs", "csc"):
        path = shutil.which(csc)
        if path and mono:
            return {"compiler": path, "runner": mono, "name": f"{csc} + mono"}
    return None


def _run_local(lang: str, code: str, stdin: str, timeout: int) -> RunResult:
    tool = local_toolchain(lang)
    if not tool:
        raise EngineUnavailable("yerel derleyici bulunamadı")
    start = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="estu_lab_") as wd:
        src_name = LANGS[lang]["file"]
        src = os.path.join(wd, src_name)
        with open(src, "w", encoding="utf-8") as f:
            f.write(code)
        if lang == "c":
            exe = os.path.join(wd, "main.exe" if os.name == "nt" else "main")
            compile_cmd = [tool["compiler"], "-Wall", "-O0", src_name, "-o", exe, "-lm"]
            run_cmd = [exe]
        else:
            exe = os.path.join(wd, "Program.exe")
            compile_cmd = [tool["compiler"], f"-out:{exe}", src_name]
            run_cmd = [tool["runner"], exe]
        try:
            comp = subprocess.run(compile_cmd, cwd=wd, capture_output=True, text=True, encoding="utf-8",
                                  errors="replace", timeout=COMPILE_TIMEOUT)
        except subprocess.TimeoutExpired:
            return RunResult(False, "timeout", stderr="Derleme zaman aşımına uğradı.", engine=f"Yerel ({tool['name']})",
                             elapsed=time.perf_counter() - start)
        comp_out = _clean_paths((comp.stdout or "") + (comp.stderr or ""), wd, src_name)
        diags = parse_diagnostics(lang, comp_out)
        if comp.returncode != 0 or not os.path.exists(exe):
            return RunResult(False, "compile", compile_output=_clip(comp_out), exit_code=comp.returncode,
                             engine=f"Yerel ({tool['name']})", elapsed=time.perf_counter() - start, diagnostics=diags)
        try:
            run = subprocess.run(run_cmd, cwd=wd, input=stdin, capture_output=True, text=True, encoding="utf-8",
                                 errors="replace", timeout=timeout)
        except subprocess.TimeoutExpired as e:
            out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
            return RunResult(False, "timeout", stdout=_clip(out),
                             stderr=f"⏱️ Program {timeout} saniye içinde bitmedi ve durduruldu (sonsuz döngü olabilir).",
                             compile_output=_clip(comp_out), engine=f"Yerel ({tool['name']})",
                             elapsed=time.perf_counter() - start, diagnostics=diags)
        return RunResult(run.returncode == 0, "run", stdout=_clip(run.stdout), stderr=_clip(run.stderr),
                         compile_output=_clip(comp_out), exit_code=run.returncode, engine=f"Yerel ({tool['name']})",
                         elapsed=time.perf_counter() - start, diagnostics=diags)


# ───────────────────────────── Katman 2: Piston ─────────────────────────────

def _run_piston(lang: str, code: str, stdin: str, timeout: int) -> RunResult:
    url = os.environ.get("PISTON_URL", PISTON_DEFAULT_URL)
    headers = {"Content-Type": "application/json"}
    token = os.environ.get("PISTON_TOKEN")
    if token:
        headers["Authorization"] = token
    payload = {
        "language": LANGS[lang]["piston"],
        "version": "*",
        "files": [{"name": LANGS[lang]["file"], "content": code}],
        "stdin": stdin,
        "compile_timeout": COMPILE_TIMEOUT * 1000,
        "run_timeout": timeout * 1000,
    }
    start = time.perf_counter()
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=HTTP_TIMEOUT)
    except requests.RequestException as e:
        raise EngineUnavailable(f"Piston'a ulaşılamadı ({e.__class__.__name__})")
    try:
        data = r.json()
    except ValueError:
        raise EngineUnavailable(f"Piston geçersiz yanıt (HTTP {r.status_code})")
    if r.status_code != 200 or "run" not in data:
        msg = data.get("message", f"HTTP {r.status_code}") if isinstance(data, dict) else f"HTTP {r.status_code}"
        raise EngineUnavailable(f"Piston reddetti: {msg[:160]}")
    elapsed = time.perf_counter() - start
    comp = data.get("compile") or {}
    comp_out = _clean_paths((comp.get("stdout") or "") + (comp.get("stderr") or ""), "", "")
    diags = parse_diagnostics(lang, comp_out)
    engine = f"Piston ({data.get('language')} {data.get('version', '')})".strip()
    if comp and comp.get("code") not in (0, None):
        return RunResult(False, "compile", compile_output=_clip(comp_out), exit_code=comp.get("code"), engine=engine,
                         elapsed=elapsed, diagnostics=diags)
    run = data["run"]
    if run.get("signal") == "SIGKILL":
        return RunResult(False, "timeout", stdout=_clip(run.get("stdout")),
                         stderr=f"⏱️ Program {timeout} saniye içinde bitmedi ve durduruldu (sonsuz döngü olabilir).",
                         compile_output=_clip(comp_out), engine=engine, elapsed=elapsed, diagnostics=diags)
    return RunResult(run.get("code") == 0, "run", stdout=_clip(run.get("stdout")), stderr=_clip(run.get("stderr")),
                     compile_output=_clip(comp_out), exit_code=run.get("code"), engine=engine, elapsed=elapsed, diagnostics=diags)


# ───────────────────────────── Katman 3: Wandbox ─────────────────────────────

_CS_MAIN = re.compile(r"(static\s+(?:async\s+)?\w+\s+Main\s*\([^)]*\)\s*\{)")


def _force_utf8_console(code: str) -> str:
    """Uzak mono sunucularında Türkçe karakterlerin '?' çıkmaması için Main'in ilk satırına UTF-8 ayarı ekler.

    Ekleme açılış süslü parantezinin hemen arkasına, aynı satıra yapılır; satır numaraları değişmez.
    """
    if "OutputEncoding" in code:
        return code
    return _CS_MAIN.sub(r"\1 System.Console.OutputEncoding = new System.Text.UTF8Encoding(false);", code, count=1)


WATCHDOG_EXIT = 124
RETRY_DELAYS = (2, 5)  # HTTP 429 / 5xx sonrası bekleme süreleri (sn)


def _post_with_retry(url: str, payload: dict, name: str, headers: dict | None = None) -> requests.Response:
    """Ücretsiz API'lerin hız sınırına (429) ve geçici 5xx hatalarına karşı geri çekilerek yeniden dener."""
    for attempt in range(len(RETRY_DELAYS) + 1):
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=HTTP_TIMEOUT)
        except requests.RequestException as e:
            if attempt == len(RETRY_DELAYS):
                raise EngineUnavailable(f"{name}'a ulaşılamadı ({e.__class__.__name__})")
        else:
            if r.status_code != 429 and r.status_code < 500 or attempt == len(RETRY_DELAYS):
                return r
            retry_after = r.headers.get("Retry-After", "")
            if retry_after.isdigit():
                time.sleep(min(int(retry_after), 15))
                continue
        time.sleep(RETRY_DELAYS[attempt])
    raise EngineUnavailable(f"{name} yanıt vermedi")


def _add_watchdog(lang: str, code: str, timeout: int) -> str:
    """Uzak sunucuda süre sınırını garantiler; ekleme satır numaralarını değiştirmez.

    C: dosyanın SONUNA alarm() kuran bir constructor eklenir (SIGALRM ile durur).
    C#: Main'in açılış satırına, süre dolunca süreci 124 koduyla bitiren arka plan iş parçacığı eklenir.
    """
    if lang == "c":
        return code.rstrip("\n") + (
            "\nunsigned int alarm(unsigned int);"
            f" __attribute__((constructor)) static void estu_watchdog__(void) {{ alarm({timeout}); }}\n")
    snippet = (" new System.Threading.Thread(() => { System.Threading.Thread.Sleep(%d); System.Console.Out.Flush();"
               " System.Environment.Exit(%d); }) { IsBackground = true }.Start();" % (timeout * 1000, WATCHDOG_EXIT))
    return _CS_MAIN.sub(lambda m: m.group(1) + snippet, code, count=1)


def _run_wandbox(lang: str, code: str, stdin: str, timeout: int) -> RunResult:
    last_err = "bilinmeyen hata"
    code = _add_watchdog(lang, code, timeout)
    for compiler in LANGS[lang]["wandbox"]:
        payload = {"compiler": compiler, "code": code, "stdin": stdin}
        if lang == "c":
            payload["options"] = "warning"
        start = time.perf_counter()
        for attempt in range(2):
            r = _post_with_retry(WANDBOX_URL, payload, "Wandbox")
            try:
                data = r.json() if r.status_code == 200 else {}
            except ValueError:
                data = {}
            blob = " ".join(str(data.get(k) or "") for k in ("compiler_error", "program_error", "program_message"))
            # Sunucu tarafı konteyner hatası (ör. "OCI runtime error: … Resource temporarily unavailable") → bir kez daha dene
            if attempt == 0 and ("OCI runtime" in blob or "Resource temporarily unavailable" in blob):
                time.sleep(RETRY_DELAYS[0])
                continue
            break
        if r.status_code == 429:
            raise EngineUnavailable("Wandbox çok fazla istek aldı (HTTP 429); birkaç saniye sonra tekrar dene")
        if r.status_code != 200 or not data:
            last_err = f"HTTP {r.status_code}: {r.text[:120]}" if r.status_code != 200 else "geçersiz yanıt"
            continue
        elapsed = time.perf_counter() - start
        comp_out = (data.get("compiler_output") or "") + (data.get("compiler_error") or "")
        comp_out = re.sub(r"\bprog\.(?:cs|cc|c)\b", LANGS[lang]["file"], comp_out)
        diags = parse_diagnostics(lang, comp_out)
        engine = f"Wandbox ({compiler})"
        prog_out = data.get("program_output") or ""
        prog_err = data.get("program_error") or ""
        status = data.get("status")
        signal = data.get("signal") or ""
        compile_failed = any(d["severity"] == "error" for d in diags) and not prog_out and not prog_err
        if compile_failed:
            return RunResult(False, "compile", compile_output=_clip(comp_out), exit_code=int(status) if str(status).lstrip("-").isdigit() else None,
                             engine=engine, elapsed=elapsed, diagnostics=diags)
        code_int = int(status) if str(status).lstrip("-").isdigit() else None
        if (signal in ("Killed", "SIGKILL", "Alarm clock", "SIGALRM", "CPU time limit exceeded")
                or code_int in (137, 142, WATCHDOG_EXIT) or "time limit" in (data.get("program_message") or "").lower()):
            return RunResult(False, "timeout", stdout=_clip(prog_out),
                             stderr=f"⏱️ Program {timeout} saniye içinde bitmedi ve durduruldu (sonsuz döngü olabilir).",
                             compile_output=_clip(comp_out), engine=engine, elapsed=elapsed, diagnostics=diags)
        if code_int is None and not signal:
            # Wandbox çıktı sınırını aşan programları durum kodu vermeden keser.
            return RunResult(False, "timeout", stdout=_clip(prog_out),
                             stderr="⏱️ Program çok fazla çıktı üretti ve sunucu tarafından durduruldu (sonsuz döngü olabilir).",
                             compile_output=_clip(comp_out), engine=engine, elapsed=elapsed, diagnostics=diags)
        if signal and code_int is None:
            prog_err = (prog_err + f"\n[sinyal: {signal}]").strip()
        return RunResult(code_int == 0 and not signal, "run", stdout=_clip(prog_out), stderr=_clip(prog_err),
                         compile_output=_clip(comp_out), exit_code=code_int, engine=engine, elapsed=elapsed, diagnostics=diags)
    raise EngineUnavailable(f"Wandbox derleyicisi çalışmadı: {last_err}")


_ENGINES = {"local": _run_local, "piston": _run_piston, "wandbox": _run_wandbox}


def run_code(lang: str, code: str, stdin: str = "", engine: str = "auto", timeout: int = RUN_TIMEOUT) -> RunResult:
    """Kodu seçilen (veya ilk uygun) katmanda derleyip çalıştırır."""
    if lang not in LANGS:
        raise ValueError(f"Desteklenmeyen dil: {lang}")
    stdin = _normalize_stdin(stdin)
    if lang == "csharp":
        code = _force_utf8_console(code)
    order = ["local", "piston", "wandbox"] if engine == "auto" else [engine]
    notes = []
    for name in order:
        try:
            res = _ENGINES[name](lang, code, stdin, timeout)
            res.notes = notes
            return res
        except EngineUnavailable as e:
            notes.append(f"{ENGINE_LABELS[name]}: {e}")
    return RunResult(False, "unavailable", stderr="Hiçbir derleme katmanı kullanılamadı.\n" + "\n".join(notes), notes=notes)


def engine_status() -> dict:
    """Arayüzde gösterilecek katman durumu (ağ çağrısı yapmadan)."""
    return {
        "c_local": (local_toolchain("c") or {}).get("name"),
        "cs_local": (local_toolchain("csharp") or {}).get("name"),
        "piston_url": os.environ.get("PISTON_URL", PISTON_DEFAULT_URL),
        "piston_token": bool(os.environ.get("PISTON_TOKEN")),
    }

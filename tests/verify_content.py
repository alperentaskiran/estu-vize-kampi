"""İçerik doğrulama: veri bütünlüğü + kod sorularının cevaplarını gerçek derleyicide kontrol eder.

Kullanım:  python tests/verify_content.py            (tüm kontroller, ağ gerekir)
           python tests/verify_content.py --offline  (sadece yapısal kontroller)
"""

import os
import sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from data.code_templates import TEMPLATES  # noqa: E402
from data.curriculum import COURSES, QUESTIONS, TEMPLATES_BY_ID, WEEK_BY_ID  # noqa: E402
from tests.code_runner import run_code  # noqa: E402

errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


def norm(text):
    return "\n".join(line.rstrip() for line in (text or "").strip().splitlines())


# ── Yapısal kontroller ──
for c in COURSES:
    n = c["question_count"]
    check(n >= 25, f"{c['id']}: sadece {n} soru var (en az 25 olmalı)")
    check(len(c["flashcards"]) >= 10, f"{c['id']}: ezber kartı az")
    for w in c["weeks"]:
        check(w["summary"].strip() and w["must"] and w["cheat"], f"{w['id']}: özet/must/cheat eksik")
        for fname, _ in w["images"]:
            check(os.path.exists(os.path.join(ROOT, "assets", fname)), f"{w['id']}: görsel yok {fname}")
        for tid in w["templates"]:
            check(tid in TEMPLATES_BY_ID, f"{w['id']}: şablon yok {tid}")

ids = set()
for q in QUESTIONS:
    check(q["id"] not in ids, f"tekrarlı id {q['id']}")
    ids.add(q["id"])
    check(q["week"] in WEEK_BY_ID, f"{q['id']}: hafta yok {q['week']}")
    check(len(q["options"]) == 4, f"{q['id']}: 4 şık olmalı")
    check(len(set(q["options"])) == 4, f"{q['id']}: şıklar tekrarlı")
    check(0 <= q["answer"] < len(q["options"]), f"{q['id']}: geçersiz cevap indeksi")
    check(q["explain"].strip(), f"{q['id']}: çözüm açıklaması yok")
    if q.get("run"):
        check(q.get("lang") in ("c", "csharp"), f"{q['id']}: run var ama lang yok")

print(f"Yapısal kontrol: {len(COURSES)} ders, {len(QUESTIONS)} soru, {len(TEMPLATES)} şablon — {len(errors)} hata")

if "--offline" not in sys.argv:
    jobs = []
    for q in QUESTIONS:
        if q.get("run"):
            jobs.append(("soru " + q["id"], q["lang"], q["run"], q.get("stdin", ""), q.get("expect"), q.get("expect_error", False),
                         q["options"][q["answer"]]))
    for t in TEMPLATES:
        jobs.append(("şablon " + t["id"], t["lang"], t["code"], t.get("stdin", ""), None, t["title"].startswith("⚠️ Hatalı"), None))

    def run(job):
        name, lang, code, stdin, expect, expect_error, answer_text = job
        return job, run_code(lang, code, stdin)

    with ThreadPoolExecutor(max_workers=1) as pool:
        results = list(pool.map(run, jobs))

    for (name, lang, code, stdin, expect, expect_error, answer_text), r in results:
        if expect_error:
            check(r.stage == "compile" and r.diagnostics, f"{name}: derleme hatası bekleniyordu, sonuç {r.stage}")
            status = "derleme hatası ✓" if r.stage == "compile" else "✗"
        elif expect is not None:
            ok = r.stage == "run" and norm(r.stdout) == norm(expect)
            check(ok, f"{name}: beklenen {expect!r}, gelen {r.stdout!r} ({r.stage}) {r.compile_output[:200]}")
            status = "✓" if ok else "✗"
        else:
            ok = r.stage in ("run", "timeout") and r.stage != "compile"
            if "dizi_tuzak" in name:  # sınır dışı yazma: çökme de geçerli bir öğretici sonuç
                ok = r.stage in ("run", "timeout")
            check(ok, f"{name}: çalışmadı ({r.stage}) {r.compile_output[:300]} {r.notes[-1:] if r.notes else r.stderr[:200]}")
            status = "✓" if ok else "✗"
        print(f"  {status:18s} {name:32s} [{r.engine}] {r.elapsed:.1f}s")

if errors:
    print("\nHATALAR:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("\nTüm kontroller başarılı ✅")

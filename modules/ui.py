"""Koyu tema CSS'i ve küçük HTML bileşenleri (kart, kutu, terminal)."""

from __future__ import annotations

import html

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
  --bg: #0b1020; --panel: #121933; --panel2: #18213f; --line: rgba(148,163,255,.14);
  --text: #e6e9f5; --muted: #9aa3c7; --accent: #7c5cff; --accent2: #22d3ee;
  --ok: #34d399; --warn: #fbbf24; --bad: #f87171;
}
html, body, [class*="css"], .stMarkdown, .stText { font-family: 'Inter', system-ui, sans-serif; }
code, pre, .stCode, textarea { font-family: 'JetBrains Mono', ui-monospace, monospace !important; }
.stApp { background: radial-gradient(1200px 600px at 10% -10%, rgba(124,92,255,.18), transparent 60%),
                     radial-gradient(900px 500px at 110% 0%, rgba(34,211,238,.12), transparent 60%), var(--bg); }
.block-container { padding-top: 1.2rem; padding-bottom: 4rem; max-width: 1280px; }
header[data-testid="stHeader"] { background: transparent; }

.hero { display:flex; flex-wrap:wrap; gap:14px; align-items:center; justify-content:space-between;
        padding: 18px 22px; border-radius: 20px; border: 1px solid var(--line);
        background: linear-gradient(135deg, rgba(124,92,255,.22), rgba(34,211,238,.10)); margin-bottom: 14px; }
.hero h1 { font-size: 1.55rem; font-weight: 800; margin: 0; letter-spacing: -.02em; color: var(--text); }
.hero p { margin: 2px 0 0; color: var(--muted); font-size: .92rem; }
.countdown { text-align:center; padding: 8px 18px; border-radius: 14px; background: rgba(11,16,32,.55); border: 1px solid var(--line); }
.countdown b { display:block; font-size: 1.9rem; line-height: 1.1; color: #fff; }
.countdown span { font-size: .78rem; color: var(--muted); }

.card { background: linear-gradient(180deg, var(--panel2), var(--panel)); border: 1px solid var(--line);
        border-radius: 16px; padding: 16px 18px; margin-bottom: 12px; }
.card h4 { margin: 0 0 6px; font-size: 1.02rem; }
.card .sub { color: var(--muted); font-size: .85rem; }
.stat { font-size: 1.6rem; font-weight: 800; }
.pill { display:inline-block; padding: 2px 10px; border-radius: 999px; font-size: .74rem; font-weight: 600;
        border: 1px solid var(--line); background: rgba(124,92,255,.15); color: #cfc6ff; margin: 2px 4px 2px 0; }
.bar { height: 8px; border-radius: 99px; background: rgba(255,255,255,.07); overflow: hidden; margin: 8px 0 4px; }
.bar > div { height: 100%; border-radius: 99px; background: linear-gradient(90deg, var(--accent), var(--accent2)); }

.must { border: 1px solid rgba(248,113,113,.45); background: linear-gradient(135deg, rgba(248,113,113,.14), rgba(251,191,36,.08));
        border-radius: 16px; padding: 14px 18px; margin: 6px 0 14px; }
.must .title { font-weight: 800; color: #fecaca; letter-spacing: .02em; margin-bottom: 6px; }
.must ul { margin: 0; padding-left: 1.1rem; } .must li { margin: 3px 0; }

.concept { background: rgba(34,211,238,.06); border: 1px solid rgba(34,211,238,.25); border-radius: 12px; padding: 10px 12px; height: 100%; }
.concept b { color: #a5f3fc; } .concept div { color: var(--text); font-size: .9rem; margin-top: 3px; }

.flash { min-height: 190px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;
         border-radius: 20px; padding: 26px; font-size: 1.15rem; font-weight: 600; border: 1px solid var(--line);
         background: linear-gradient(135deg, rgba(124,92,255,.28), rgba(24,33,63,.9)); }
.flash.back { background: linear-gradient(135deg, rgba(52,211,153,.22), rgba(24,33,63,.9)); }
.flash small { color: var(--muted); font-weight: 500; font-size: .78rem; margin-bottom: 10px; letter-spacing: .08em; }

.term { background: #05070f; border: 1px solid #1f2a4d; border-radius: 14px; overflow: hidden; }
.term .head { display:flex; gap:8px; align-items:center; padding: 8px 12px; background: #0d1326; border-bottom: 1px solid #1f2a4d;
              font-size: .78rem; color: var(--muted); flex-wrap: wrap; }
.term .dot { width: 10px; height: 10px; border-radius: 50%; display:inline-block; }
.term pre { margin: 0; padding: 12px 14px; color: #d1fae5; font-size: .86rem; white-space: pre-wrap; word-break: break-word;
            max-height: 420px; overflow: auto; background: transparent; }
.term pre.err { color: #fecaca; } .term pre.comp { color: #fde68a; }
.codeview { background: #05070f; border: 1px solid #1f2a4d; border-radius: 12px; padding: 8px 0; font-family: 'JetBrains Mono', monospace;
            font-size: .82rem; overflow-x: auto; max-height: 360px; overflow-y: auto; }
.codeview .ln { display:block; padding: 0 12px; white-space: pre; color: #cbd5e1; }
.codeview .ln i { display:inline-block; width: 2.6em; color: #475569; font-style: normal; user-select: none; }
.codeview .ln.error { background: rgba(248,113,113,.18); border-left: 3px solid var(--bad); }
.codeview .ln.warning { background: rgba(251,191,36,.12); border-left: 3px solid var(--warn); }

.qcard { background: linear-gradient(180deg, var(--panel2), var(--panel)); border: 1px solid var(--line); border-radius: 18px; padding: 18px 20px; }
.qmeta { color: var(--muted); font-size: .8rem; margin-bottom: 6px; }
.qtext { font-size: 1.08rem; font-weight: 600; line-height: 1.5; }

textarea { font-size: .9rem !important; line-height: 1.45 !important; }
div[data-testid="stSegmentedControl"] button { font-weight: 600; }
.stTabs [data-baseweb="tab-list"] { flex-wrap: wrap; gap: 4px; }

@media (max-width: 640px) {
  .block-container { padding-left: .7rem; padding-right: .7rem; padding-top: .6rem; }
  .hero { padding: 14px; } .hero h1 { font-size: 1.2rem; }
  .countdown b { font-size: 1.4rem; }
  .card, .qcard { padding: 12px 13px; }
  .qtext { font-size: 1rem; }
  .flash { min-height: 150px; font-size: 1rem; padding: 18px; }
}
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def esc(text) -> str:
    return html.escape(str(text))


def hero(title: str, subtitle: str, days_left: int) -> None:
    if days_left > 0:
        cd = f"<b>{days_left}</b><span>gün kaldı · 9 Kasım</span>"
    elif days_left == 0:
        cd = "<b>BUGÜN</b><span>vizeler başlıyor — başarılar!</span>"
    else:
        cd = "<b>🎯</b><span>vize dönemi</span>"
    st.markdown(f"""<div class="hero"><div><h1>{esc(title)}</h1><p>{esc(subtitle)}</p></div>
<div class="countdown">{cd}</div></div>""", unsafe_allow_html=True)


def progress_bar(ratio: float) -> str:
    pct = max(0, min(100, round(ratio * 100)))
    return f'<div class="bar"><div style="width:{pct}%"></div></div>'


def must_box(items: list[str]) -> None:
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    st.markdown(f'<div class="must"><div class="title">🎯 SINAVDA KESİN ÇIKAR</div><ul>{lis}</ul></div>', unsafe_allow_html=True)


def concept_grid(concepts: list[tuple[str, str]], cols: int = 3) -> None:
    for i in range(0, len(concepts), cols):
        row = st.columns(cols)
        for col, (term, desc) in zip(row, concepts[i:i + cols]):
            col.markdown(f'<div class="concept"><b>{esc(term)}</b><div>{esc(desc)}</div></div>', unsafe_allow_html=True)
        st.write("")


def table_md(columns: list[str], rows: list[list[str]]) -> str:
    def cell(v):
        return str(v).replace("|", "\\|").replace("\n", "<br>")
    out = ["| " + " | ".join(cell(c) for c in columns) + " |", "|" + "---|" * len(columns)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def code_view(code: str, diagnostics: list[dict]) -> None:
    """Satır numaralı kod; hata/uyarı satırları renklendirilir."""
    marks = {}
    for d in diagnostics:
        if d["severity"] == "error" or d["line"] not in marks:
            marks[d["line"]] = d["severity"]
    lines = []
    for n, line in enumerate(code.split("\n"), 1):
        cls = marks.get(n, "")
        lines.append(f'<span class="ln {cls}"><i>{n}</i>{esc(line) or " "}</span>')
    st.html(f'<div class="codeview">{"".join(lines)}</div>')


def terminal(result) -> None:
    color = {"run": "#34d399" if result.ok else "#fbbf24", "compile": "#f87171", "timeout": "#fbbf24", "unavailable": "#f87171"}[result.stage]
    status = {"run": "Çalıştı" if result.ok else f"Çalıştı (çıkış kodu {result.exit_code})", "compile": "Derleme hatası",
              "timeout": "Zaman aşımı", "unavailable": "Motor yok"}[result.stage]
    head = (f'<div class="head"><span class="dot" style="background:{color}"></span><b style="color:{color}">{status}</b>'
            f'<span>· {esc(result.engine or "—")}</span><span>· {result.elapsed:.1f} sn</span></div>')

    def pre(text: str) -> str:
        return esc(text.rstrip()).replace("\r", "")

    body = ""
    if result.compile_output.strip():
        body += f'<pre class="comp">$ derleyici\n{pre(result.compile_output)}</pre>'
    if result.stage != "compile":
        out = result.stdout if result.stdout else ("(çıktı yok)" if result.stage == "run" else "")
        if out:
            body += f"<pre>$ ./program\n{pre(out)}</pre>"
    if result.stderr.strip():
        body += f'<pre class="err">{pre(result.stderr)}</pre>'
    st.html(f'<div class="term">{head}{body}</div>')

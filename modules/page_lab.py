"""💻 Ders Kodları: derslerde anlatılan C / C# örneklerinin salt-okunur, ortalanmış kod editörü görünümü.

Kod çalıştırma bilinçli olarak yok — uygulama hafif kalsın diye kodlar yalnızca okunur, kopyalanır ve indirilir.
"""

from __future__ import annotations

import streamlit as st

from data.curriculum import COURSE_BY_ID, COURSES, TEMPLATES, TEMPLATES_BY_ID
from modules import ui
from modules.state import LANG_LABELS, PAGE_NOTES

FILE_NAMES = {"c": "main.c", "csharp": "Program.cs"}
FILTERS = {"all": "Tümü", "c": "⚙️ C", "cs": "🟣 C#", "other": "🧮 Diğer"}

# Şablon → ilgili ders haftası (Ders Özetleri'ne geri dönüş için)
_WEEK_OF = {tid: (c["id"], w["title"]) for c in COURSES for w in c["weeks"] for tid in w["templates"]}


def _filtered(key: str) -> list[str]:
    if key == "c":
        return [t["id"] for t in TEMPLATES if t["course"] == "c"]
    if key == "cs":
        return [t["id"] for t in TEMPLATES if t["course"] == "cs"]
    if key == "other":
        return [t["id"] for t in TEMPLATES if t["course"] not in ("c", "cs")]
    return [t["id"] for t in TEMPLATES]


def _pick() -> None:
    st.session_state.lab_template = st.session_state.lab_pick


def _filter_changed() -> None:
    ss = st.session_state
    ids = _filtered(ss.lab_filter or "all")
    if ss.lab_template not in ids:
        ss.lab_template = ids[0]


def _step(ids: list[str], delta: int) -> None:
    ss = st.session_state
    cur = ss.lab_template if ss.lab_template in ids else ids[0]
    ss.lab_template = ids[(ids.index(cur) + delta) % len(ids)]


def _go_notes(course_id: str) -> None:
    st.session_state.notes_course = course_id
    st.session_state.nav = PAGE_NOTES


def _editor(title: str, lang: str, code: str, meta: str, stdin: str = "") -> None:
    lines = code.rstrip("\n").count("\n") + 1
    st.html(f"""<div class="ed-tab">
  <div class="ed-dots"><span style="background:#f87171"></span><span style="background:#fbbf24"></span><span style="background:#34d399"></span></div>
  <div class="ed-file">📄 {ui.esc(FILE_NAMES[lang])}</div>
  <div class="ed-title">{ui.esc(title)}</div>
  <div class="ed-lang">{LANG_LABELS[lang]} · {lines} satır</div>
</div>""")
    with st.container(key="code_editor"):
        st.code(code, language="c" if lang == "c" else "csharp", line_numbers=True)
    st.html(f'<div class="ed-status"><span>{ui.esc(meta)}</span>'
            + (f'<span>⌨️ Örnek girdi (stdin): <b>{ui.esc(stdin)}</b></span>' if stdin else "") + "</div>")


def render() -> None:
    ss = st.session_state
    _, center, _ = st.columns([1, 10, 1])
    with center:
        # Widget değerleri her çalıştırmada, widget'tan ÖNCE yeniden yazılır (önceki çalıştırmada atanan
        # anahtarların tarayıcıda boş görünmesi sorununa karşı).
        ss.lab_filter = ss.get("lab_filter") or "all"
        ids = _filtered(ss.lab_filter)
        if ss.lab_template not in ids:
            if ss.lab_template in TEMPLATES_BY_ID:  # başka dersten açıldıysa filtreyi genişlet
                ss.lab_filter, ids = "all", _filtered("all")
            else:
                ss.lab_template = ids[0]
        ss.lab_pick = ss.lab_template

        top = st.columns([1, 2])
        top[0].segmented_control("Ders", list(FILTERS), format_func=FILTERS.get, key="lab_filter", on_change=_filter_changed,
                                  label_visibility="collapsed")
        top[1].selectbox("Kod", ids, key="lab_pick", on_change=_pick, label_visibility="collapsed",
                         format_func=lambda tid: f"[{COURSE_BY_ID[TEMPLATES_BY_ID[tid]['course']]['short']}] {TEMPLATES_BY_ID[tid]['title']}")

        t = TEMPLATES_BY_ID[ss.lab_template]
        week = _WEEK_OF.get(t["id"])
        meta = f"📎 Kaynak: {t['source']}" + (f" · 📚 {week[1]}" if week else "")
        _editor(t["title"], t["lang"], t["code"], meta, t.get("stdin", ""))

        pos = ids.index(t["id"])
        nav = st.columns([1, 1.3, 1.3, 1])
        nav[0].button("⬅️ Önceki", on_click=_step, args=(ids, -1), width="stretch")
        nav[1].download_button("⬇️ Dosyayı indir", t["code"], file_name=FILE_NAMES[t["lang"]], width="stretch")
        if week:
            nav[2].button("📚 Konu özetine git", on_click=_go_notes, args=(week[0],), width="stretch")
        nav[3].button("Sonraki ➡️", on_click=_step, args=(ids, 1), width="stretch")
        st.caption(f"{pos + 1} / {len(ids)} kod · Kodu kopyalamak için editörün sağ üstündeki kopyala simgesini kullan.")

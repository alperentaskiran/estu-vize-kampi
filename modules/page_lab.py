"""💻 C & C# Kod Laboratuvarı: dil seçici, ders şablonları, editör, stdin, derle-çalıştır, terminal."""

from __future__ import annotations

import re

import streamlit as st

from data.curriculum import COURSE_BY_ID, TEMPLATES_BY_ID, templates_for
from modules import ui
from modules.code_sandbox import ENGINE_LABELS, LANGS, run_code
from modules.state import LANG_LABELS, restore_lab_widgets, save_lab_widgets

STARTERS = {
    "c": '#include <stdio.h>\n\nint main() {\n    \n    return 0;\n}\n',
    "csharp": 'using System;\n\nclass Program\n{\n    static void Main()\n    {\n        \n    }\n}\n',
}
_NEEDS_INPUT = {"c": re.compile(r"\b(scanf|getchar|fgets|gets)\s*\("), "csharp": re.compile(r"Console\.(ReadLine|Read|ReadKey)\s*\(")}


def _load_template() -> None:
    ss = st.session_state
    tid = ss.get("lab_pick")
    if tid:
        t = TEMPLATES_BY_ID[tid]
        ss.lab_lang, ss.lab_code, ss.lab_stdin, ss.lab_template, ss.lab_result = t["lang"], t["code"], t.get("stdin", ""), tid, None


def _change_lang() -> None:
    ss = st.session_state
    if ss.lab_lang is None:  # seçili dile tekrar tıklanınca seçim kalkar → eski dile dön
        ss.lab_lang = ss.lab_saved["lab_lang"]
        return
    ss.lab_code = STARTERS[ss.lab_lang]
    ss.lab_stdin = ""
    ss.lab_template = None
    ss.lab_result = None
    ss.lab_pick = None


def _clear() -> None:
    ss = st.session_state
    ss.lab_code = STARTERS[ss.lab_lang]
    ss.lab_stdin = ""
    ss.lab_result = None
    ss.lab_template = None


def render() -> None:
    ss = st.session_state
    restore_lab_widgets()
    top = st.columns([1, 2.2, 1.2])
    top[0].segmented_control("Dil", ["c", "csharp"], format_func=LANG_LABELS.get, key="lab_lang", on_change=_change_lang)

    temps = templates_for(lang=ss.lab_lang)
    ids = [t["id"] for t in temps]
    if ss.get("lab_pick") not in ids:
        ss.lab_pick = ss.lab_template if ss.lab_template in ids else None
    top[1].selectbox("📂 Ders şablonları", ids, key="lab_pick", placeholder="Derslerdeki hazır kodlardan birini seç…",
                     format_func=lambda tid: f"[{COURSE_BY_ID[TEMPLATES_BY_ID[tid]['course']]['short']}] {TEMPLATES_BY_ID[tid]['title']}",
                     on_change=_load_template)
    top[2].selectbox("⚙️ Motor", list(ENGINE_LABELS), format_func=ENGINE_LABELS.get, key="lab_engine")

    if ss.lab_template and ss.lab_template in TEMPLATES_BY_ID:
        t = TEMPLATES_BY_ID[ss.lab_template]
        st.caption(f"📎 Şablon: **{t['title']}** — kaynak: {t['source']}")

    left, right = st.columns([1.15, 1], gap="medium")
    with left:
        st.text_area(f"✏️ Kod editörü ({LANGS[ss.lab_lang]['label']} · {LANGS[ss.lab_lang]['file']})", key="lab_code", height=430)
        needs_input = bool(_NEEDS_INPUT[ss.lab_lang].search(ss.lab_code))
        st.text_area("⌨️ Program Girdisi (Stdin)" + (" — bu kod girdi okuyor!" if needs_input else ""), key="lab_stdin", height=90,
                     placeholder="scanf / Console.ReadLine için girdiler (her satıra bir değer veya boşlukla ayır)")
        if needs_input and not ss.lab_stdin.strip():
            st.warning("Kod `scanf`/`Console.ReadLine` içeriyor ama Stdin boş — program girdi bekleyip boş değer okuyabilir.")
        b = st.columns([1.6, 1, 1])
        run_clicked = b[0].button("▶️ Derle ve Çalıştır", type="primary", width="stretch")
        b[1].button("🧹 Temizle", on_click=_clear, width="stretch")
        b[2].download_button("⬇️ İndir", ss.lab_code, file_name=LANGS[ss.lab_lang]["file"], width="stretch")
        if run_clicked:
            with st.spinner("Derleniyor ve çalıştırılıyor…"):
                ss.lab_result = run_code(ss.lab_lang, ss.lab_code, ss.lab_stdin, engine=ss.lab_engine)
            ss.lab_ran_code = ss.lab_code
    save_lab_widgets()

    with right:
        st.markdown("**🖥️ Terminal**")
        res = ss.lab_result
        if res is None:
            st.markdown('<div class="term"><div class="head"><span class="dot" style="background:#475569"></span>'
                        '<span>Hazır — kodu yazıp ▶️ Derle ve Çalıştır\'a bas.</span></div><pre>$ _</pre></div>', unsafe_allow_html=True)
            st.caption("Derleme sırası: yerel gcc/mono → Piston API → Wandbox API. Çalışma süresi sınırı 5 sn.")
        else:
            ui.terminal(res)
            if res.diagnostics:
                errs = [d for d in res.diagnostics if d["severity"] == "error"]
                warns = [d for d in res.diagnostics if d["severity"] == "warning"]
                st.markdown(f"**🔎 Derleyici bulguları:** {len(errs)} hata · {len(warns)} uyarı")
                st.dataframe([{"Satır": d["line"], "Sütun": d["col"], "Tür": "❌ hata" if d["severity"] == "error" else "⚠️ uyarı",
                               "Kod": d["code"], "Mesaj": d["message"]} for d in res.diagnostics],
                             hide_index=True, width="stretch")
                ui.code_view(ss.get("lab_ran_code", ss.lab_code), res.diagnostics)
                if any("expected ';'" in d["message"] or "before" in d["message"] or d["code"] in ("CS1002", "CS1525") for d in errs):
                    st.info("İpucu: `;` eksik hatası çoğu zaman **gösterilen satırın bir öncesindeki** satırdan kaynaklanır.")
            if res.notes:
                with st.expander("Motor geçiş notları"):
                    for n in res.notes:
                        st.caption("• " + n)

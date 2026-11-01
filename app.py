"""ESTÜ Vize Kampı — Bulut Bilişim Operatörlüğü çalışma platformu ve gömülü C/C# derleyici laboratuvarı.

Çalıştırma:  streamlit run app.py
"""

import os
from datetime import date

import streamlit as st

st.set_page_config(page_title="ESTÜ Vize Kampı", page_icon="🎓", layout="wide", initial_sidebar_state="collapsed")

# Streamlit Cloud secrets → ortam değişkenleri (Piston kendi sunucu/token desteği için)
try:
    for _k in ("PISTON_URL", "PISTON_TOKEN"):
        if _k in st.secrets and not os.environ.get(_k):
            os.environ[_k] = str(st.secrets[_k])
except Exception:  # secrets.toml yoksa st.secrets erişimi hata verebilir
    pass

from data.curriculum import COURSES, EXAM_START, QUESTIONS, TEMPLATES  # noqa: E402
from modules import page_cockpit, page_exam, page_lab, page_notes, state, ui  # noqa: E402

state.init()
ui.inject_css()

ui.hero("🎓 ESTÜ Vize Kampı · Bulut Bilişim Operatörlüğü",
        f"{len(COURSES)} ders · {len(QUESTIONS)} vize provası sorusu · {len(TEMPLATES)} hazır C/C# kodu · gömülü derleyici",
        (EXAM_START - date.today()).days)

st.segmented_control("Sayfa", state.PAGES, key="nav", label_visibility="collapsed")
current = state.track_navigation()

PAGES = {
    state.PAGE_COCKPIT: page_cockpit.render,
    state.PAGE_NOTES: page_notes.render,
    state.PAGE_LAB: page_lab.render,
    state.PAGE_EXAM: page_exam.render,
}
PAGES[current]()

st.caption("Ders içerikleri canvas_materyalleri/ klasöründeki PDF, PPTX, DOCX ve PNG dosyalarından derlenmiştir.")

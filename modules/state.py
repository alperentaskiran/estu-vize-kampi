"""Sayfalar arası paylaşılan oturum durumu ve geri çağırımlar (callbacks)."""

from __future__ import annotations

import random

import streamlit as st

PAGE_COCKPIT = "📊 Vize Kokpiti"
PAGE_NOTES = "📚 Ders Özetleri"
PAGE_LAB = "💻 Ders Kodları"
PAGE_EXAM = "📝 Sınav & Yanlışlarım"
PAGES = [PAGE_COCKPIT, PAGE_NOTES, PAGE_LAB, PAGE_EXAM]

LANG_LABELS = {"c": "C", "csharp": "C#"}


def init() -> None:
    ss = st.session_state
    ss.setdefault("nav", PAGE_COCKPIT)
    ss.setdefault("_last_nav", ss.nav)
    ss.setdefault("lab_template", "c_merhaba")
    ss.setdefault("exam", None)
    ss.setdefault("exam_notice", None)


def track_navigation() -> str:
    """Geçerli sayfayı döndürür; sınav sekmesine başka sekmeden dönülünce aktif sınavı Soru 1'e sıfırlar."""
    ss = st.session_state
    page = ss.nav or ss._last_nav  # segmented_control seçimi kaldırılırsa son sayfada kal
    if page == PAGE_EXAM and ss._last_nav != PAGE_EXAM:
        reset_exam_state(keep_questions=True)
    ss._last_nav = page
    return page


# ── Ders kodları ──
def open_in_lab(template_id: str) -> None:
    """'💻 Editörde Aç' düğmeleri için callback: kodu Ders Kodları editöründe gösterir."""
    st.session_state.lab_template = template_id
    st.session_state.nav = PAGE_LAB


# ── Sınav motoru ──
def new_exam(question_ids: list[str], retry_mode: bool, title: str, options_count: dict[str, int]) -> None:
    rng = random.Random()
    order = {qid: rng.sample(range(n), n) for qid, n in options_count.items()}
    st.session_state.exam = {
        "qids": question_ids, "idx": 0, "answers": {}, "order": order, "retry": retry_mode, "title": title,
        "nonce": rng.randrange(10**9), "finished": False, "saved": False,
    }


def reset_exam_state(keep_questions: bool = False) -> None:
    """Aktif sınavı Soru 1'e döndürür (cevaplar silinir). keep_questions=False ise sınav tamamen kapatılır."""
    ss = st.session_state
    exam = ss.get("exam")
    if not exam:
        return
    if not keep_questions or exam.get("finished"):
        ss.exam = None
        return
    if exam["idx"] > 0 or exam["answers"]:
        ss.exam_notice = "Sınav sekmesinden ayrıldığın için deneme **Soru 1'e sıfırlandı** (cevaplar temizlendi)."
    exam.update({"idx": 0, "answers": {}, "nonce": random.randrange(10**9), "finished": False, "saved": False})

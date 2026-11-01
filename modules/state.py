"""Sayfalar arası paylaşılan oturum durumu ve geri çağırımlar (callbacks)."""

from __future__ import annotations

import random

import streamlit as st

from data.code_templates import BY_ID as TEMPLATES

PAGE_COCKPIT = "📊 Vize Kokpiti"
PAGE_NOTES = "📚 Ders Özetleri"
PAGE_LAB = "💻 Kod Lab (C/C#)"
PAGE_EXAM = "📝 Sınav & Yanlışlarım"
PAGES = [PAGE_COCKPIT, PAGE_NOTES, PAGE_LAB, PAGE_EXAM]

LANG_LABELS = {"c": "C", "csharp": "C#"}


# Lab widget'larının anahtarları. Widget, değeri önceki bir çalıştırmada atanmış bir anahtarla İLK KEZ
# oluşturulduğunda tarayıcı bu değeri göstermeyebiliyor; bu yüzden değerler widget'tan bağımsız `lab_saved`
# sözlüğünde tutulur ve Lab sekmesine her girişte widget anahtarlarına yeniden yazılır.
LAB_KEYS = ("lab_lang", "lab_code", "lab_stdin", "lab_engine")


def init() -> None:
    ss = st.session_state
    ss.setdefault("nav", PAGE_COCKPIT)
    ss.setdefault("_last_nav", ss.nav)
    ss.setdefault("page_entered", True)
    ss.setdefault("lab_saved", {"lab_lang": "c", "lab_code": TEMPLATES["c_merhaba"]["code"], "lab_stdin": "", "lab_engine": "auto"})
    ss.setdefault("lab_template", "c_merhaba")
    ss.setdefault("lab_result", None)
    ss.setdefault("exam", None)
    ss.setdefault("exam_notice", None)


def track_navigation() -> str:
    """Geçerli sayfayı döndürür; sınav sekmesine başka sekmeden dönülünce aktif sınavı Soru 1'e sıfırlar."""
    ss = st.session_state
    page = ss.nav or ss._last_nav  # segmented_control seçimi kaldırılırsa son sayfada kal
    if page == PAGE_EXAM and ss._last_nav != PAGE_EXAM:
        reset_exam_state(keep_questions=True)
    ss.page_entered = page != ss._last_nav
    ss._last_nav = page
    return page


def restore_lab_widgets() -> None:
    """Lab sekmesine girişte (veya anahtar kaybolduysa) widget değerlerini yedekten yazar."""
    ss = st.session_state
    for k in LAB_KEYS:
        if ss.page_entered or ss.get(k) is None:
            ss[k] = ss.lab_saved[k]


def save_lab_widgets() -> None:
    ss = st.session_state
    ss.lab_saved.update({k: ss[k] for k in LAB_KEYS if ss.get(k) is not None})


# ── Kod laboratuvarı ──
def open_in_lab(template_id: str | None = None, code: str | None = None, lang: str | None = None, stdin: str = "") -> None:
    """'💻 Editörde Aç' düğmeleri için callback: kodu editöre yükleyip Lab sekmesine geçer."""
    ss = st.session_state
    if template_id:
        t = TEMPLATES[template_id]
        code, lang, stdin = t["code"], t["lang"], t.get("stdin", "")
        ss.lab_template = template_id
    else:
        ss.lab_template = None
    ss.lab_saved.update({"lab_lang": lang, "lab_code": code, "lab_stdin": stdin})
    ss.lab_result = None
    ss.nav = PAGE_LAB
    ss._last_nav = None  # aynı sayfadan çağrılsa bile Lab'a "giriş" sayılsın → widget'lar yedekten yüklenir


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

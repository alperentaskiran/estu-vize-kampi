"""Arayüz testleri (Streamlit AppTest): tüm sayfalar hatasız açılır, sınav sıfırlama ve yanlışlar havuzu çalışır.

Kullanım:  python -m pytest tests/test_app.py -q
"""

import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ["ESTU_PROGRESS_DIR"] = tempfile.mkdtemp(prefix="estu_test_")

from streamlit.testing.v1 import AppTest  # noqa: E402

from data.curriculum import COURSES, QUESTION_BY_ID  # noqa: E402
from modules.state import PAGE_COCKPIT, PAGE_EXAM, PAGE_LAB, PAGE_NOTES  # noqa: E402

APP = os.path.join(ROOT, "app.py")


def _app():
    at = AppTest.from_file(APP, default_timeout=60)
    at.run()
    assert not at.exception, at.exception
    return at


def _goto(at, page):
    at.session_state["nav"] = page
    at.run()
    assert not at.exception, at.exception


def test_all_pages_render():
    at = _app()
    assert any("Vize" in m.label for m in at.metric)
    for page in (PAGE_NOTES, PAGE_LAB, PAGE_EXAM, PAGE_COCKPIT):
        _goto(at, page)


def test_every_course_notes_render():
    at = _app()
    _goto(at, PAGE_NOTES)
    for c in COURSES:
        at.session_state["notes_course"] = c["id"]
        at.run()
        assert not at.exception, (c["id"], at.exception)
        for view in ("⚡ Cheat Sheet", "🃏 Ezber Kartları"):
            at.session_state[f"notes_view_{c['id']}"] = view
            at.run()
            assert not at.exception, (c["id"], view, at.exception)


def test_open_in_editor_switches_to_lab():
    at = _app()
    _goto(at, PAGE_NOTES)
    at.session_state["notes_course"] = "c"
    at.run()
    btn = next(b for b in at.button if b.label == "💻 Editörde Aç")
    btn.click().run()
    assert not at.exception, at.exception
    assert at.session_state["nav"] == PAGE_LAB
    assert "int main" in at.code[0].value  # editörde dersin kodu gösteriliyor


def test_code_page_is_read_only_and_browsable():
    at = _app()
    at.button_group[0].set_value(PAGE_LAB).run()
    assert not at.exception, at.exception
    assert not at.text_area  # kod çalıştırma / düzenleme alanı yok
    assert not any("Derle" in b.label for b in at.button)
    assert "int main" in at.code[0].value

    at.button_group(key="lab_filter").set_value("cs").run()
    assert at.session_state["lab_template"].startswith("cs_") and "class Program" in at.code[0].value
    first = at.session_state["lab_template"]
    next(b for b in at.button if b.label == "Sonraki ➡️").click().run()
    assert at.session_state["lab_template"] != first
    next(b for b in at.button if b.label == "⬅️ Önceki").click().run()
    assert at.session_state["lab_template"] == first

    at.selectbox(key="lab_pick").set_value("cs_kafe").run()
    assert "decimal" in at.code[0].value
    at.button_group[0].set_value(PAGE_COCKPIT).run()
    at.button_group[0].set_value(PAGE_LAB).run()
    assert "decimal" in at.code[0].value  # sekme değişince seçili kod korunur

    next(b for b in at.button if b.label == "📚 Konu özetine git").click().run()
    assert at.session_state["nav"] == PAGE_NOTES and at.session_state["notes_course"] == "cs"


def _start_exam(at):
    _goto(at, PAGE_EXAM)
    next(b for b in at.button if b.label == "🚀 Denemeyi başlat").click().run()
    assert not at.exception, at.exception
    exam = at.session_state["exam"]
    assert exam and exam["idx"] == 0
    return exam


def _answer(at, wrong: bool):
    exam = at.session_state["exam"]
    qid = exam["qids"][exam["idx"]]
    q = QUESTION_BY_ID[qid]
    order = exam["order"][qid]
    correct_pos = order.index(q["answer"])
    pos = (correct_pos + 1) % len(order) if wrong else correct_pos
    at.radio[0].set_value(pos).run()
    next(b for b in at.button if b.label == "✔️ Cevapla").click().run()
    assert not at.exception, at.exception
    return qid


def test_exam_resets_to_question_one_after_tab_switch_and_tracks_wrong_answers():
    at = _app()
    _start_exam(at)
    wrong_qid = _answer(at, wrong=True)
    assert wrong_qid in at.session_state["progress"]["wrong_pool"]
    next(b for b in at.button if b.label == "Sonraki soru ➡️").click().run()
    assert at.session_state["exam"]["idx"] == 1

    _goto(at, PAGE_LAB)      # başka sekmeye geç
    _goto(at, PAGE_EXAM)     # geri dön → Soru 1
    exam = at.session_state["exam"]
    assert exam["idx"] == 0 and exam["answers"] == {}
    assert any("Soru 1'e sıfırlandı" in i.value for i in at.info)


def test_retry_mode_removes_correctly_answered_question():
    at = _app()
    _start_exam(at)
    qid = _answer(at, wrong=True)
    next(b for b in at.button if b.label == "⏹️ Denemeyi iptal et").click().run()
    at.session_state["exam_mode"] = "❌ Tekrar Çözülecekler"
    at.run()
    next(b for b in at.button if b.label == "🔁 Tüm yanlışlarımı çöz").click().run()
    exam = at.session_state["exam"]
    pool_before = set(at.session_state["progress"]["wrong_pool"])
    assert exam["retry"] and qid in exam["qids"] and set(exam["qids"]) == pool_before
    first = _answer(at, wrong=False)
    assert first not in at.session_state["progress"]["wrong_pool"]
    assert len(at.session_state["progress"]["wrong_pool"]) == len(pool_before) - 1


def test_finish_exam_records_attempt():
    at = _app()
    _start_exam(at)
    total = len(at.session_state["exam"]["qids"])
    for i in range(total):
        _answer(at, wrong=(i % 3 == 0))
        label = "Sonraki soru ➡️" if i + 1 < total else "🏁 Denemeyi bitir"
        next(b for b in at.button if b.label == label).click().run()
        assert not at.exception, at.exception
    attempts = at.session_state["progress"]["attempts"]
    assert attempts and attempts[-1]["total"] == total
    _goto(at, PAGE_COCKPIT)  # istatistik grafikleri hatasız çizilmeli

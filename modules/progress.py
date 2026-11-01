"""Kalıcı ilerleme kaydı: konu takibi, yanlışlar havuzu, deneme sınavı geçmişi, ezber kartları.

Veriler `.progress/progress.json` dosyasında tutulur (git'e girmez). Streamlit Cloud'da dosya sistemi
uygulama yeniden başlatılana kadar kalıcıdır; kalıcı yedek için Kokpit'teki dışa/içe aktarma kullanılır.
"""

from __future__ import annotations

import json
import os
import threading
from datetime import datetime

import streamlit as st

PROGRESS_DIR = os.environ.get("ESTU_PROGRESS_DIR") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".progress")
PROGRESS_FILE = os.path.join(PROGRESS_DIR, "progress.json")
_LOCK = threading.Lock()


def _empty() -> dict:
    return {"topics_done": {}, "wrong_pool": {}, "answered": {}, "attempts": [], "flash_known": {}}


def _read_file() -> dict:
    try:
        with open(PROGRESS_FILE, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return _empty()
    base = _empty()
    base.update({k: v for k, v in data.items() if k in base})
    return base


def get() -> dict:
    if "progress" not in st.session_state:
        st.session_state.progress = _read_file()
    return st.session_state.progress


def save() -> None:
    data = get()
    with _LOCK:
        try:
            os.makedirs(PROGRESS_DIR, exist_ok=True)
            tmp = PROGRESS_FILE + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
            os.replace(tmp, PROGRESS_FILE)
        except OSError:
            pass  # salt okunur ortamda ilerleme oturum içinde kalır


def now() -> str:
    return datetime.now().isoformat(timespec="seconds")


# ── Konu takibi ──
def topic_done(week_id: str) -> bool:
    return bool(get()["topics_done"].get(week_id))


def set_topic(week_id: str, done: bool) -> None:
    get()["topics_done"][week_id] = bool(done)
    save()


# ── Soru istatistikleri & yanlışlar havuzu ──
def record_answer(qid: str, correct: bool, retry_mode: bool) -> None:
    p = get()
    stat = p["answered"].setdefault(qid, {"seen": 0, "correct": 0})
    stat["seen"] += 1
    stat["correct"] += int(correct)
    if correct:
        if retry_mode and qid in p["wrong_pool"]:
            del p["wrong_pool"][qid]
    else:
        item = p["wrong_pool"].setdefault(qid, {"count": 0})
        item["count"] += 1
        item["last"] = now()
    save()


def remove_wrong(qid: str) -> None:
    get()["wrong_pool"].pop(qid, None)
    save()


def clear_wrong(course_id: str | None = None) -> None:
    p = get()
    if course_id is None:
        p["wrong_pool"] = {}
    else:
        p["wrong_pool"] = {k: v for k, v in p["wrong_pool"].items() if not k.startswith(course_id + "-")}
    save()


def add_attempt(attempt: dict) -> None:
    get()["attempts"].append(attempt)
    save()


# ── Ezber kartları ──
def flash_known(course_id: str) -> set:
    return set(get()["flash_known"].get(course_id, []))


def toggle_flash(course_id: str, idx: int, known: bool) -> None:
    known_set = flash_known(course_id)
    (known_set.add if known else known_set.discard)(idx)
    get()["flash_known"][course_id] = sorted(known_set)
    save()


# ── Yedekleme ──
def export_json() -> str:
    return json.dumps(get(), ensure_ascii=False, indent=1)


def import_json(text: str) -> None:
    data = json.loads(text)
    base = _empty()
    base.update({k: v for k, v in data.items() if k in base})
    st.session_state.progress = base
    save()


def reset_all() -> None:
    st.session_state.progress = _empty()
    save()

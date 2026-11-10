"""Tüm derslerin tek giriş noktası.

Her ders kendi modülünde (course_*.py) COURSE + QUESTIONS olarak tutulur; burada birleştirilir
ve sorulara kalıcı kimlik (id) atanır. Kimlikler ilerleme dosyasında (yanlışlar havuzu) kullanılır.
"""

from datetime import date

from . import course_ag, course_bt, course_c, course_cs, course_donanim, course_mat
from .code_templates import BY_ID as TEMPLATES_BY_ID
from .code_templates import TEMPLATES

EXAM_START = date(2026, 11, 9)

_MODULES = [course_bt, course_donanim, course_ag, course_c, course_cs, course_mat]

COURSES = []
QUESTIONS = []
for _m in _MODULES:
    _course = dict(_m.COURSE)
    _qs = []
    for _i, _q in enumerate(_m.QUESTIONS, 1):
        _q = dict(_q)
        _q["id"] = f"{_course['id']}-{_i:03d}"
        _q["course"] = _course["id"]
        if _q.get("run") and not _q.get("lang"):
            _q["lang"] = "csharp" if _course["id"] == "cs" else "c"
        _qs.append(_q)
    _course["question_count"] = len(_qs)
    COURSES.append(_course)
    QUESTIONS.extend(_qs)

COURSE_BY_ID = {c["id"]: c for c in COURSES}
QUESTION_BY_ID = {q["id"]: q for q in QUESTIONS}
WEEK_BY_ID = {w["id"]: (c, w) for c in COURSES for w in c["weeks"]}


def questions_for(course_ids=None, week_ids=None):
    """Ders ve/veya hafta filtresine uyan sorular."""
    out = QUESTIONS
    if course_ids:
        out = [q for q in out if q["course"] in course_ids]
    if week_ids:
        out = [q for q in out if q["week"] in week_ids]
    return out


def templates_for(lang=None, course_id=None):
    out = TEMPLATES
    if lang:
        out = [t for t in out if t["lang"] == lang]
    if course_id:
        out = [t for t in out if t["course"] == course_id]
    return out


def all_topics():
    """Kokpit takibi için (ders_id, hafta_id, başlık) listesi."""
    return [(c["id"], w["id"], w["title"]) for c in COURSES for w in c["weeks"]]

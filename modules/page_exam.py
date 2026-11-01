"""📝 Vize Sınav Simülatörü & Yanlışlarım.

- Sekmeden ayrılıp geri dönünce aktif deneme Soru 1'e sıfırlanır (state.track_navigation → reset_exam_state).
- Yanlış cevaplanan sorular kalıcı 'Tekrar Çözülecekler' havuzuna eklenir; havuz modunda doğru çözülen soru havuzdan çıkar.
"""

from __future__ import annotations

import random

import streamlit as st

from data.curriculum import COURSE_BY_ID, COURSES, QUESTION_BY_ID, WEEK_BY_ID, questions_for
from modules import progress, ui
from modules.state import new_exam, reset_exam_state

LETTERS = "ABCDE"


def _start(qids: list[str], retry: bool, title: str) -> None:
    new_exam(qids, retry, title, {qid: len(QUESTION_BY_ID[qid]["options"]) for qid in qids})


def _setup() -> None:
    p = progress.get()
    st.markdown("### 🧪 Yeni deneme oluştur")
    course_ids = st.multiselect("Dersler", [c["id"] for c in COURSES], default=[c["id"] for c in COURSES],
                                format_func=lambda cid: f"{COURSE_BY_ID[cid]['icon']} {COURSE_BY_ID[cid]['name']}")
    week_opts = [w["id"] for c in COURSES if c["id"] in course_ids for w in c["weeks"]]
    week_ids = st.multiselect("Haftalar (boş = hepsi)", week_opts, format_func=lambda wid: WEEK_BY_ID[wid][1]["title"])
    pool = questions_for(course_ids, week_ids)
    c1, c2 = st.columns(2)
    n_max = len(pool)
    if n_max == 0:
        st.warning("Seçime uyan soru yok.")
        return
    count = c1.slider("Soru sayısı", 1, n_max, min(20, n_max))
    only_new = c2.toggle("Önce hiç çözmediklerim", help="Daha önce cevaplanmamış soruları öne alır.")
    st.caption(f"Havuzda {n_max} soru var.")
    if st.button("🚀 Denemeyi başlat", type="primary", width="stretch"):
        rng = random.Random()
        ids = [q["id"] for q in pool]
        rng.shuffle(ids)
        if only_new:
            ids.sort(key=lambda qid: qid in p["answered"])
        names = ", ".join(COURSE_BY_ID[c]["short"] for c in course_ids)
        _start(ids[:count], False, f"Deneme · {names}")
        st.rerun()


def _question(exam: dict) -> None:
    qid = exam["qids"][exam["idx"]]
    q = QUESTION_BY_ID[qid]
    course = COURSE_BY_ID[q["course"]]
    total = len(exam["qids"])
    answered = exam["answers"].get(qid)

    st.progress((exam["idx"] + (1 if answered else 0)) / total, text=f"Soru {exam['idx'] + 1} / {total}")
    st.markdown(f"""<div class="qcard"><div class="qmeta">{course['icon']} {ui.esc(course['name'])} · {ui.esc(WEEK_BY_ID[q['week']][1]['title'])}</div>
<div class="qtext">{ui.esc(q['q'])}</div></div>""", unsafe_allow_html=True)
    if q.get("code"):
        st.code(q["code"], language="c" if q.get("lang") == "c" else "csharp")
    if q.get("stdin"):
        st.caption(f"⌨️ Program girdisi (stdin): `{q['stdin']}`")

    order = exam["order"][qid]
    labels = [f"{LETTERS[i]}) {q['options'][o]}" for i, o in enumerate(order)]
    key = f"{exam['nonce']}_{qid}"
    choice = st.radio("Cevabın", range(len(order)), format_func=lambda i: labels[i], index=None if answered is None else answered["shown"],
                      key=f"ans_{key}", disabled=answered is not None, label_visibility="collapsed")

    if answered is None:
        st.button("✔️ Cevapla", type="primary", disabled=choice is None, width="stretch", key=f"submit_{key}",
                  on_click=_submit, args=(qid, f"ans_{key}"))
        return

    right_shown = order.index(q["answer"])
    if answered["correct"]:
        st.success(f"✅ Doğru! Cevap **{LETTERS[right_shown]}**." + (" Bu soru Tekrar Çözülecekler havuzundan çıkarıldı." if exam["retry"] else ""))
    else:
        st.error(f"❌ Yanlış. Doğru cevap **{LETTERS[right_shown]}) {q['options'][q['answer']]}** — soru *Tekrar Çözülecekler* havuzuna eklendi.")
    st.markdown(f"**💡 Çözüm:** {q['explain']}")

    nav = st.columns(2)
    if exam["idx"] + 1 < total:
        nav[1].button("Sonraki soru ➡️", type="primary", width="stretch", key=f"next_{key}", on_click=_next)
    else:
        nav[1].button("🏁 Denemeyi bitir", type="primary", width="stretch", key=f"finish_{key}", on_click=_finish)
    nav[0].button("⏹️ Denemeyi iptal et", width="stretch", key=f"cancel_{key}", on_click=reset_exam_state)


def _submit(qid: str, radio_key: str) -> None:
    exam = st.session_state.exam
    shown = st.session_state.get(radio_key)
    if not exam or shown is None or qid in exam["answers"]:
        return
    correct = exam["order"][qid][shown] == QUESTION_BY_ID[qid]["answer"]
    exam["answers"][qid] = {"shown": shown, "correct": correct}
    progress.record_answer(qid, correct, exam["retry"])


def _next() -> None:
    exam = st.session_state.exam
    if exam and exam["idx"] + 1 < len(exam["qids"]):
        exam["idx"] += 1


def _finish() -> None:
    if st.session_state.exam:
        st.session_state.exam["finished"] = True


def _summary(exam: dict) -> None:
    total = len(exam["qids"])
    correct = sum(a["correct"] for a in exam["answers"].values())
    if not exam["saved"]:
        progress.add_attempt({"ts": progress.now(), "title": exam["title"], "total": total, "correct": correct, "retry": exam["retry"]})
        exam["saved"] = True
    pct = round(100 * correct / total) if total else 0
    st.markdown(f"""<div class="card"><h4>🏁 {ui.esc(exam['title'])} tamamlandı</h4>
<div class="stat">{correct} / {total} · %{pct}</div>{ui.progress_bar(correct / total if total else 0)}
<div class="sub">{'Harika! Vizeye hazırsın. 🚀' if pct >= 85 else 'İyi gidiyor — yanlışlarını tekrar çöz.' if pct >= 60 else 'Konu anlatımına dönüp yanlışlarını tekrar et.'}</div></div>""",
                unsafe_allow_html=True)
    by_course = {}
    for qid in exam["qids"]:
        cid = QUESTION_BY_ID[qid]["course"]
        ok = exam["answers"].get(qid, {}).get("correct", False)
        t = by_course.setdefault(cid, [0, 0])
        t[0] += ok
        t[1] += 1
    st.dataframe([{"Ders": COURSE_BY_ID[c]["name"], "Doğru": v[0], "Soru": v[1], "%": round(100 * v[0] / v[1])} for c, v in by_course.items()],
                 hide_index=True, width="stretch")
    wrong = [qid for qid in exam["qids"] if not exam["answers"].get(qid, {}).get("correct")]
    if wrong:
        st.markdown("#### ❌ Yanlışların")
        for qid in wrong:
            q = QUESTION_BY_ID[qid]
            with st.expander(q["q"]):
                if q.get("code"):
                    st.code(q["code"], language="c" if q.get("lang") == "c" else "csharp")
                st.markdown(f"**Doğru cevap:** {q['options'][q['answer']]}\n\n{q['explain']}")
    c1, c2 = st.columns(2)
    if c1.button("🔁 Aynı soruları yeniden çöz", width="stretch"):
        _start(random.sample(exam["qids"], len(exam["qids"])), exam["retry"], exam["title"])
        st.rerun()
    if c2.button("🧪 Yeni deneme", type="primary", width="stretch"):
        reset_exam_state()
        st.rerun()


def _wrong_pool() -> None:
    pool = progress.get()["wrong_pool"]
    if not pool:
        st.success("Tekrar Çözülecekler havuzun boş. Deneme çözdükçe yanlışların burada birikir.")
        return
    by_course = {}
    for qid, info in pool.items():
        if qid in QUESTION_BY_ID:
            by_course.setdefault(QUESTION_BY_ID[qid]["course"], []).append((qid, info))
    st.markdown(f"**{len(pool)} soru** tekrar çözülmeyi bekliyor. Havuz modunda doğru çözdüğün soru otomatik silinir.")
    a, b = st.columns(2)
    if a.button("🔁 Tüm yanlışlarımı çöz", type="primary", width="stretch"):
        ids = list(pool)
        random.shuffle(ids)
        _start([i for i in ids if i in QUESTION_BY_ID], True, "Tekrar Çözülecekler")
        st.rerun()
    if b.button("🗑️ Havuzu temizle", width="stretch"):
        progress.clear_wrong()
        st.rerun()
    for cid, items in by_course.items():
        c = COURSE_BY_ID[cid]
        st.markdown(f"#### {c['icon']} {c['name']} — {len(items)}")
        if st.button(f"🔁 Sadece {c['short']} yanlışlarını çöz", key=f"retry_{cid}"):
            _start([qid for qid, _ in items], True, f"Tekrar · {c['short']}")
            st.rerun()
        for qid, info in sorted(items, key=lambda kv: -kv[1].get("count", 0)):
            q = QUESTION_BY_ID[qid]
            with st.expander(f"×{info.get('count', 1)} · {q['q']}"):
                if q.get("code"):
                    st.code(q["code"], language="c" if q.get("lang") == "c" else "csharp")
                st.markdown(f"**Doğru cevap:** {q['options'][q['answer']]}\n\n**Çözüm:** {q['explain']}")
                if st.button("Havuzdan çıkar", key=f"rm_{qid}"):
                    progress.remove_wrong(qid)
                    st.rerun()


def render() -> None:
    ss = st.session_state
    if ss.get("exam_notice"):
        st.info(ss.exam_notice, icon="🔄")
        ss.exam_notice = None

    pool_n = len(progress.get()["wrong_pool"])
    mode = st.segmented_control("Bölüm", ["📝 Sınav Simülatörü", "❌ Tekrar Çözülecekler"], default="📝 Sınav Simülatörü",
                                key="exam_mode", label_visibility="collapsed")
    st.caption(f"Tekrar Çözülecekler havuzunda **{pool_n}** soru var.")
    exam = ss.get("exam")
    if mode == "❌ Tekrar Çözülecekler" and not exam:
        _wrong_pool()
        return
    if not exam:
        _setup()
    elif exam["finished"]:
        _summary(exam)
    else:
        st.caption(f"🧪 {exam['title']}" + (" · havuz modu" if exam["retry"] else ""))
        _question(exam)

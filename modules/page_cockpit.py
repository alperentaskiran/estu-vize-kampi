"""📊 9 Kasım Vize Kokpiti: ders listesi, konu takibi, deneme istatistikleri, motor durumu."""

from __future__ import annotations

from datetime import date, datetime

import pandas as pd
import streamlit as st

from data.curriculum import COURSE_BY_ID, COURSES, EXAM_START, QUESTION_BY_ID, QUESTIONS
from modules import progress, ui
from modules.state import PAGE_EXAM, PAGE_NOTES


def _go(page: str, course_id: str | None = None) -> None:
    st.session_state.nav = page
    if course_id:
        st.session_state.notes_course = course_id


def _course_stats(course_id: str) -> dict:
    p = progress.get()
    weeks = COURSE_BY_ID[course_id]["weeks"]
    done = sum(progress.topic_done(w["id"]) for w in weeks)
    qids = [q["id"] for q in QUESTIONS if q["course"] == course_id]
    seen = sum(p["answered"].get(q, {}).get("seen", 0) for q in qids)
    correct = sum(p["answered"].get(q, {}).get("correct", 0) for q in qids)
    covered = sum(1 for q in qids if q in p["answered"])
    wrong = sum(1 for q in p["wrong_pool"] if q.startswith(course_id + "-"))
    return {"weeks": len(weeks), "done": done, "questions": len(qids), "covered": covered, "seen": seen,
            "accuracy": correct / seen if seen else None, "wrong": wrong}


def render() -> None:
    p = progress.get()
    days_left = (EXAM_START - date.today()).days
    total_weeks = sum(len(c["weeks"]) for c in COURSES)
    done_weeks = sum(progress.topic_done(w["id"]) for c in COURSES for w in c["weeks"])
    seen = sum(v["seen"] for v in p["answered"].values())
    correct = sum(v["correct"] for v in p["answered"].values())

    m = st.columns(4)
    m[0].metric("Vize başlangıcı", "9 Kasım", f"{days_left} gün" if days_left >= 0 else "başladı", delta_color="off", delta_arrow="off", border=True)
    m[1].metric("Konu tamamlama", f"%{round(100 * done_weeks / total_weeks)}", f"{done_weeks}/{total_weeks} hafta", delta_color="off", delta_arrow="off", border=True)
    m[2].metric("Çözülen soru", seen, f"%{round(100 * correct / seen)} doğru" if seen else "henüz yok", delta_color="off", delta_arrow="off", border=True)
    m[3].metric("Tekrar çözülecek", len(p["wrong_pool"]), f"{len(QUESTIONS)} soruluk banka", delta_color="off", delta_arrow="off", border=True)

    st.subheader("Dersler")
    cols = st.columns(3)
    for i, c in enumerate(COURSES):
        s = _course_stats(c["id"])
        acc = f"%{round(100 * s['accuracy'])} başarı" if s["accuracy"] is not None else "deneme yok"
        with cols[i % 3]:
            st.markdown(f"""<div class="card"><h4>{c['icon']} {ui.esc(c['name'])}</h4>
<div class="sub">{s['done']}/{s['weeks']} konu · {s['questions']} soru · {acc} · ❌ {s['wrong']}</div>
{ui.progress_bar(s['done'] / s['weeks'])}
<div class="sub">Soru kapsamı: {s['covered']}/{s['questions']}</div>{ui.progress_bar(s['covered'] / s['questions'])}</div>""",
                        unsafe_allow_html=True)
            b1, b2 = st.columns(2)
            b1.button("📚 Çalış", key=f"ck_n_{c['id']}", on_click=_go, args=(PAGE_NOTES, c["id"]), width="stretch")
            b2.button("📝 Test", key=f"ck_e_{c['id']}", on_click=_go, args=(PAGE_EXAM,), width="stretch")

    left, right = st.columns([1.1, 1])
    with left:
        st.subheader("✅ Konu tamamlama takibi")
        for c in COURSES:
            s = _course_stats(c["id"])
            with st.expander(f"{c['icon']} {c['name']} — {s['done']}/{s['weeks']}"):
                for w in c["weeks"]:
                    val = st.checkbox(w["title"], value=progress.topic_done(w["id"]), key=f"topic_{w['id']}")
                    if val != progress.topic_done(w["id"]):
                        progress.set_topic(w["id"], val)
                        st.rerun()
    with right:
        st.subheader("📈 Deneme sınavı istatistikleri")
        attempts = p["attempts"]
        if not attempts:
            st.info("Henüz deneme çözmedin. **📝 Sınav & Yanlışlarım** sekmesinden ilk denemeni başlat.")
        else:
            df = pd.DataFrame(attempts)
            df["Tarih"] = pd.to_datetime(df["ts"]).dt.strftime("%d.%m %H:%M")
            df["Başarı %"] = (100 * df["correct"] / df["total"]).round(0)
            st.line_chart(df.set_index("Tarih")["Başarı %"], height=180)
            show = df[["Tarih", "title", "correct", "total", "Başarı %"]].rename(columns={"title": "Deneme", "correct": "Doğru", "total": "Soru"})
            st.dataframe(show.iloc[::-1], hide_index=True, width="stretch", height=220)
        per_course = []
        for c in COURSES:
            s = _course_stats(c["id"])
            if s["accuracy"] is not None:
                per_course.append({"Ders": c["short"], "Başarı %": round(100 * s["accuracy"])})
        if per_course:
            st.caption("Ders bazında doğruluk (tüm cevaplar)")
            st.bar_chart(pd.DataFrame(per_course).set_index("Ders"), height=180)

    st.subheader("🧠 En çok zorlandığın sorular")
    hard = sorted(p["wrong_pool"].items(), key=lambda kv: -kv[1].get("count", 0))[:5]
    if not hard:
        st.caption("Yanlışlar havuzu boş — harika gidiyorsun ya da henüz test çözmedin.")
    for qid, info in hard:
        q = QUESTION_BY_ID.get(qid)
        if q:
            st.markdown(f"- **{COURSE_BY_ID[q['course']]['short']}** · {ui.esc(q['q'])} *(×{info.get('count', 1)})*")

    with st.expander("💾 İlerleme yedeği"):
        c1, c2, c3 = st.columns(3)
        c1.download_button("⬇️ İlerlemeyi indir", progress.export_json(), file_name=f"estu_ilerleme_{datetime.now():%Y%m%d}.json",
                           mime="application/json", width="stretch")
        up = c2.file_uploader("İlerleme yükle", type="json", label_visibility="collapsed")
        if up is not None and c2.button("⬆️ Yüklemeyi uygula", width="stretch"):
            try:
                progress.import_json(up.getvalue().decode("utf-8"))
                st.success("İlerleme yüklendi.")
                st.rerun()
            except ValueError:
                st.error("Geçersiz dosya.")
        if c3.button("🗑️ Tüm ilerlemeyi sıfırla", width="stretch"):
            progress.reset_all()
            st.rerun()

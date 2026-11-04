"""📚 Ders Özetleri & Cheat Sheets: konu anlatımı, kavram kartları, görseller, hızlı tekrar, ezber kartları."""

from __future__ import annotations

import os
import random

import streamlit as st

from data.curriculum import COURSE_BY_ID, COURSES, TEMPLATES_BY_ID
from modules import progress, ui
from modules.state import LANG_LABELS, open_in_lab

ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")


def _week_view(course: dict, week: dict) -> None:
    top = st.columns([3, 1])
    top[0].caption("📎 Kaynak: " + " · ".join(week["sources"]))
    done = top[1].toggle("Tamamlandı", value=progress.topic_done(week["id"]), key=f"done_{week['id']}")
    if done != progress.topic_done(week["id"]):
        progress.set_topic(week["id"], done)

    ui.must_box(week["must"])
    with st.container(key=f"lesson_{week['id']}"):
        st.markdown(week["summary"])

    if week["concepts"]:
        st.markdown("#### 🔑 Kritik kavramlar")
        ui.concept_grid(week["concepts"])

    if week["images"]:
        st.markdown("#### 🖼️ Ders görselleri ve diyagramlar")
        for i in range(0, len(week["images"]), 2):
            row = st.columns(2)
            for col, (fname, caption) in zip(row, week["images"][i:i + 2]):
                path = os.path.join(ASSETS, fname)
                if os.path.exists(path):
                    col.image(path, caption=caption, width="stretch")

    if week["templates"]:
        st.markdown("#### 💻 Bu konunun örnek kodları")
        for tid in week["templates"]:
            t = TEMPLATES_BY_ID[tid]
            with st.expander(f"{LANG_LABELS[t['lang']]} · {t['title']}  —  {t['source']}"):
                st.code(t["code"], language="c" if t["lang"] == "c" else "csharp", line_numbers=True)
                st.button("💻 Editörde Aç", key=f"open_{week['id']}_{tid}", on_click=open_in_lab, kwargs={"template_id": tid})


def _cheat_sheet(course: dict) -> None:
    st.markdown(f"### ⚡ {course['name']} — Hızlı Tekrar")
    for week in course["weeks"]:
        st.markdown(f"**{week['title']}**")
        cols = st.columns([1, 1.4])
        with cols[0]:
            ui.must_box(week["must"])
        with cols[1]:
            for tbl in week["cheat"]:
                st.markdown(f"*{tbl['title']}*")
                st.markdown(ui.table_md(tbl["columns"], tbl["rows"]), unsafe_allow_html=True)
        st.divider()


def _flashcards(course: dict) -> None:
    cards = course["flashcards"]
    key = f"fc_{course['id']}"
    ss = st.session_state
    ss.setdefault(key + "_order", list(range(len(cards))))
    ss.setdefault(key + "_pos", 0)
    ss.setdefault(key + "_flip", False)
    known = progress.flash_known(course["id"])

    only_unknown = st.toggle("Sadece bilmediklerim", key=key + "_only")
    order = [i for i in ss[key + "_order"] if not (only_unknown and i in known)]
    if not order:
        st.success("Bu destedeki tüm kartları biliyorsun! 🎉")
        return
    ss[key + "_pos"] %= len(order)
    idx = order[ss[key + "_pos"]]
    front, back = cards[idx]

    st.caption(f"Kart {ss[key + '_pos'] + 1}/{len(order)} · Bilinen: {len(known)}/{len(cards)}")
    if ss[key + "_flip"]:
        st.markdown(f'<div class="flash back"><small>CEVAP</small>{ui.esc(back)}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="flash"><small>SORU</small>{ui.esc(front)}</div>', unsafe_allow_html=True)

    def flip():
        ss[key + "_flip"] = not ss[key + "_flip"]

    def move(step):
        ss[key + "_pos"] = (ss[key + "_pos"] + step) % len(order)
        ss[key + "_flip"] = False

    def shuffle():
        random.shuffle(ss[key + "_order"])
        ss[key + "_pos"] = 0
        ss[key + "_flip"] = False

    def mark(val):
        progress.toggle_flash(course["id"], idx, val)
        move(1)

    b = st.columns(5)
    b[0].button("⬅️", key=key + "_prev", on_click=move, args=(-1,), width="stretch")
    b[1].button("🔄 Çevir", key=key + "_flipb", on_click=flip, width="stretch")
    b[2].button("➡️", key=key + "_next", on_click=move, args=(1,), width="stretch")
    if idx in known:
        b[3].button("↩️ Bilmiyorum", key=key + "_unk", on_click=mark, args=(False,), width="stretch")
    else:
        b[3].button("✅ Biliyorum", key=key + "_kn", on_click=mark, args=(True,), width="stretch")
    b[4].button("🔀 Karıştır", key=key + "_sh", on_click=shuffle, width="stretch")


def render() -> None:
    ss = st.session_state
    ss.setdefault("notes_course", COURSES[0]["id"])
    options = [c["id"] for c in COURSES]
    course_id = st.pills("Ders", options, format_func=lambda cid: f"{COURSE_BY_ID[cid]['icon']} {COURSE_BY_ID[cid]['name']}",
                         key="notes_course", label_visibility="collapsed")
    course = COURSE_BY_ID[course_id or options[0]]
    st.caption(f"{course['teacher'] + ' · ' if course['teacher'] else ''}Kaynak dosyalar: " + ", ".join(course["sources"]))

    view = st.segmented_control("Görünüm", ["📖 Konu Anlatımı", "⚡ Cheat Sheet", "🃏 Ezber Kartları"], default="📖 Konu Anlatımı",
                                key=f"notes_view_{course['id']}", label_visibility="collapsed")
    if view == "⚡ Cheat Sheet":
        _cheat_sheet(course)
    elif view == "🃏 Ezber Kartları":
        _flashcards(course)
    else:
        tabs = st.tabs([w["title"].split(" — ")[0] for w in course["weeks"]])
        for tab, week in zip(tabs, course["weeks"]):
            with tab:
                st.markdown(f"### {week['title']}")
                _week_view(course, week)

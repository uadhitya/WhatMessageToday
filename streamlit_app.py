"""
streamlit_app.py — Web UI untuk sistem WhatMessageToday.
"""

import streamlit as st
from datetime import datetime

# --- 1. DATA INTEGRITY ---
try:
    from yawm_logic import (
        calculate_yawm_index, get_yawm_data, get_tafsir_indices,
        YEAR_MIN, YEAR_MAX
    )
except ImportError:
    st.error("Error: Module yawm_logic tidak ditemukan.")
    st.stop()

# --- 2. CSS FINAL (CLEAN INDUSTRIAL) ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; }
    .main-title { color: #ffffff; font-size: 2.5rem; font-weight: 800; margin-bottom: 20px; }
    .header-card {
        background: linear-gradient(90deg, #161b22 0%, #0b0e14 100%);
        padding: 25px;
        border-radius: 12px;
        border-bottom: 2px solid #3b82f6;
        margin-bottom: 30px;
    }
    .day-num { color: #ffffff; font-size: 3.5rem; font-weight: 900; line-height: 1; }
    .year-tag { color: #3b82f6; font-size: 1rem; font-weight: 700; letter-spacing: 2px; }

    .msg-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .ref-id { color: #f59e0b; font-family: monospace; font-weight: bold; font-size: 1rem; }
    .message-text { color: #e6edf3; font-size: 1.2rem; line-height: 1.6; margin-top: 10px; }
    
    .label-sebab { color: #ff7b72; font-weight: bold; text-transform: uppercase; font-size: 0.9rem; margin: 20px 0 10px 0; }
    .label-petunjuk { color: #7ee787; font-weight: bold; text-transform: uppercase; font-size: 0.9rem; margin: 20px 0 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. JUDUL & INPUT (POSISI UTAMA) ---
st.markdown("<div class='main-title'>WhatMessageToday</div>", unsafe_allow_html=True)

target_date = st.date_input(
    "OPERATIONAL DATE AUDIT", 
    value=datetime.now(),
    min_value=datetime(YEAR_MIN, 1, 1),
    max_value=datetime(YEAR_MAX, 12, 31)
)

hari_ke, n = calculate_yawm_index(target_date)
sebab_idx, petunjuk_idx = get_tafsir_indices(n)

# --- 4. HEADER CHRONOLOGY ---
st.markdown(f"""
    <div class='header-card'>
        <div class='year-tag'>SYSTEM CHRONOLOGY {target_date.year}</div>
        <div class='day-num'>DAY {n} <span style='font-size:1rem; color:#8b949e;'>(Hari ke-{hari_ke} dari epoch)</span></div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. DATA DISPLAY ---
data = get_yawm_data(n)
if data:
    st.markdown(f"""
        <div class='msg-card' style='border-left: 4px solid #3b82f6;'>
            <span class='ref-id'>ID: {data[0]} {data[1]}:{data[2]}</span>
            <div class='message-text'><i><b>"{data[3]}"</b></i></div>
        </div>
        """, unsafe_allow_html=True)

# --- 6. TAFSIR SECTION ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='label-sebab'>TAFSIR SEBAB</div>", unsafe_allow_html=True)
    for idx in sebab_idx:
        v = get_yawm_data(idx)
        if v:
            st.markdown(f"""
                <div class='msg-card'>
                    <span class='ref-id' style='font-size:0.85rem;'>{v[0]} {v[1]}:{v[2]}</span>
                    <div class='message-text' style='font-size:1rem;'><i>"{v[3]}"</i></div>
                </div>
                """, unsafe_allow_html=True)

with col2:
    st.markdown("<div class='label-petunjuk'>TAFSIR PETUNJUK</div>", unsafe_allow_html=True)
    for idx in petunjuk_idx:
        v = get_yawm_data(idx)
        if v:
            st.markdown(f"""
                <div class='msg-card'>
                    <span class='ref-id' style='font-size:0.85rem;'>{v[0]} {v[1]}:{v[2]}</span>
                    <div class='message-text' style='font-size:1rem;'><i>"{v[3]}"</i></div>
                </div>
                """, unsafe_allow_html=True)

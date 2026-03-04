import streamlit as st
from datetime import datetime

# --- 1. DATA INTEGRITY ---
try:
    from database_yawm import DATA_YAWM
except:
    DATA_YAWM = {}

def get_indices(n):
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    petunjuk = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, petunjuk

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
    min_value=datetime(1900, 1, 1),
    max_value=datetime(2200, 12, 31)
)

day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
sebab_idx, petunjuk_idx = get_indices(n)

# --- 4. HEADER CHRONOLOGY ---
st.markdown(f"""
    <div class='header-card'>
        <div class='year-tag'>SYSTEM CHRONOLOGY {target_date.year}</div>
        <div class='day-num'>DAY {n}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. DATA DISPLAY ---
if n in DATA_YAWM:
    d = DATA_YAWM[n]
    st.markdown(f"""
        <div class='msg-card' style='border-left: 4px solid #3b82f6;'>
            <span class='ref-id'>ID: {d[0]} {d[1]}:{d[2]}</span>
            <div class='message-text'><i><b>"{d[-1]}"</b></i></div>
        </div>
        """, unsafe_allow_html=True)

# --- 6. TAFSIR SECTION ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='label-sebab'>TAFSIR SEBAB</div>", unsafe_allow_html=True)
    for idx in sebab_idx:
        if idx in DATA_YAWM:
            v = DATA_YAWM[idx]
            st.markdown(f"""
                <div class='msg-card'>
                    <span class='ref-id' style='font-size:0.85rem;'>{v[0]} {v[1]}:{v[2]}</span>
                    <div class='message-text' style='font-size:1rem;'><i>"{v[-1]}"</i></div>
                </div>
                """, unsafe_allow_html=True)

with col2:
    st.markdown("<div class='label-petunjuk'>TAFSIR PETUNJUK</div>", unsafe_allow_html=True)
    for idx in petunjuk_idx:
        if idx in DATA_YAWM:
            v = DATA_YAWM[idx]
            st.markdown(f"""
                <div class='msg-card'>
                    <span class='ref-id' style='font-size:0.85rem;'>{v[0]} {v[1]}:{v[2]}</span>
                    <div class='message-text' style='font-size:1rem;'><i>"{v[-1]}"</i></div>
                </div>
                """, unsafe_allow_html=True)

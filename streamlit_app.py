import streamlit as st
from datetime import datetime

# --- 1. LOGIKA INTI (HARGA MATI) ---
try:
    from database_yawm import DATA_YAWM
except:
    DATA_YAWM = {}

def get_indices(n):
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    perbaikan = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, perbaikan

# --- 2. ESTETIKA FUNGSIONAL (DESIGN TANPA MERUSAK) ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .main-card { background: #161b22; border-radius: 8px; padding: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    .day-label { color: #8b949e; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; }
    .day-value { color: #ffffff; font-size: 2.2rem; font-weight: 700; margin-bottom: 10px; }
    .arabic { font-family: 'Amiri', serif; direction: rtl; text-align: right; font-size: 2rem; line-height: 1.8; color: #f0f2f6; }
    .latin { font-style: italic; color: #9ca3af; font-size: 1.1rem; border-left: 2px solid #3b82f6; padding-left: 15px; }
    .ref { color: #3b82f6; font-weight: 600; font-size: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INPUT PERIOD (1900-2200) ---
target_date = st.date_input(
    "Audit Date", 
    value=datetime.now(),
    min_value=datetime(1900, 1, 1),
    max_value=datetime(2200, 12, 31)
)

n = target_date.timetuple().tm_yday
n = 365 if n > 365 else n
tahun = target_date.year
sebab_idx, perbaikan_idx = get_indices(n)

# --- 4. DISPLAY UTAMA ---
st.markdown(f"<div class='day-label'>Log Operasional</div>", unsafe_allow_html=True)
st.markdown(f"<div class='day-value'>Day {n}, {tahun}</div>", unsafe_allow_html=True)

if n in DATA_YAWM:
    d = DATA_YAWM[n]
    with st.container():
        st.markdown(f"<div class='main-card'><span class='ref'>{d[0]} {d[1]}:{d[2]}</span>", unsafe_allow_html=True)
        if len(d) >= 5:
            st.markdown(f"<p class='arabic'>{d[3]}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='latin'>{d[4]}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- 5. TAFSIR (3-COLUMNS) ---
for label, indices in [("Tafsir Sebab", sebab_idx), ("Tafsir Perbaikan", perbaikan_idx)]:
    st.markdown(f"### {label}")
    cols = st.columns(3)
    for i, idx in enumerate(indices):
        with cols[i]:
            if idx in DATA_YAWM:
                v = DATA_YAWM[idx]
                st.markdown(f"<div class='main-card'><span class='ref'>{v[0]} {v[1]}:{v[2]}</span>", unsafe_allow_html=True)
                if len(v) >= 5:
                    st.markdown(f"<p class='arabic' style='font-size:1.4rem;'>{v[3]}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p class='latin' style='font-size:0.9rem;'>{v[4]}</p>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

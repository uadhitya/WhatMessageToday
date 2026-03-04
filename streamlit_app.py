import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE (Logika Asli) ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    DATA_YAWM = {}

# --- 2. LOGIKA INDEKS (Sistem Sakral) ---
def get_indices(n):
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    perbaikan = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, perbaikan

# --- 3. FINAL DESIGN SETTINGS (UI/UX Audit) ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")

st.markdown("""
    <style>
    /* Tipografi Global */
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Skala Heading yang Diperhalus */
    h1 { font-size: 2.2rem !important; font-weight: 800; letter-spacing: -1px; }
    h2 { font-size: 1.5rem !important; color: #3b82f6; } /* Highlight untuk Day Pusat */
    h3 { font-size: 1.1rem !important; font-weight: 700; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px; }
    
    /* Box Container Audit */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 4px !important;
        padding: 20px !important;
    }
    
    /* Styling Identitas vs Kutipan */
    .identitas { font-weight: 700; font-size: 1rem; color: #ffffff; }
    .kutipan { font-style: italic; font-size: 0.95rem; color: #d1d5db; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ANTARMUKA UTAMA ---
st.markdown("# WhatMessageToday")

# Input di Area Utama (Sesuai Struktur Asli)
target_date = st.date_input("Audit Period", value=datetime.now())

day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
sebab_indices, perbaikan_indices = get_indices(n)

st.write("") # Spacer

# --- 5. TITIK PUSAT (Day N) ---
if n in DATA_YAWM:
    d = DATA_YAWM[n]
    st.markdown(f"## Day {n} Tahun Ini")
    st.markdown(f"<p class='identitas'>{d[0]} {d[1]}:{d[2]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='kutipan'>\"{d[3]}\"</p>", unsafe_allow_html=True)
else:
    st.info(f"Day {n} | Log data belum tersedia dalam sistem.")

st.write("") # Spacer

# --- 6. TAFSIR SEBAB (3-in-1 Box) ---
with st.container(border=True):
    st.markdown("### Tafsir Sebab")
    cols = st.columns(3)
    for i, idx in enumerate(sebab_indices):
        with cols[i]:
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.markdown(f"<p class='identitas'>{d[0]} {d[1]}:{d[2]}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='kutipan'>\"{d[3]}\"</p>", unsafe_allow_html=True)
            else:
                st.caption("*Data belum diinput*")

# --- 7. TAFSIR PERBAIKAN (3-in-1 Box) ---
with st.container(border=True):
    st.markdown("### Tafsir Perbaikan")
    cols = st.columns(3)
    for i, idx in enumerate(perbaikan_indices):
        with cols[i]:
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.markdown(f"<p class='identitas'>{d[0]} {d[1]}:{d[2]}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='kutipan'>\"{d[3]}\"</p>", unsafe_allow_html=True)
            else:
                st.caption("*Data belum diinput*")

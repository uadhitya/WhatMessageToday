import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    DATA_YAWM = {}

# --- 2. LOGIKA INDEKS (LOGIKA SAKRAL) ---
def get_indices(n):
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    perbaikan = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, perbaikan

# --- 3. AUDIT DESIGN: GLOBAL UI SETTINGS ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")

# CSS untuk membenahi hierarki dan estetika tanpa merubah sistem
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1, h2, h3 { color: #ffffff; letter-spacing: -0.5px; }
    .stMarkdown p { font-size: 1.05rem; line-height: 1.6; color: #d1d5db; }
    /* Menghilangkan padding berlebih agar box terlihat padat */
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    /* Styling khusus untuk ayat agar menonjol secara elegan */
    .ayat-text { font-style: italic; color: #9ca3af; border-left: 2px solid #3b82f6; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("WhatMessageToday")

# Sidebar untuk input agar area utama tetap bersih
with st.sidebar:
    st.markdown("### Parameter Audit")
    target_date = st.date_input("Audit Period", value=datetime.now(),
                                min_value=datetime(1900, 1, 1),
                                max_value=datetime(2200, 12, 31))

day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
sebab_indices, perbaikan_indices = get_indices(n)

st.write("---")

# --- 4. TITIK PUSAT (AUDIT POINT) ---
if n in DATA_YAWM:
    d = DATA_YAWM[n]
    st.markdown(f"## Day {n} | Index {n}")
    st.markdown(f"### {d[0]} {d[1]}:{d[2]}")
    st.markdown(f'<p class="ayat-text">{d[3]}</p>', unsafe_allow_html=True)
else:
    st.warning(f"Day {n} | Index {n} - Data belum terintegrasi dalam sistem.")

st.write("---")

# --- 5. BOX TAFSIR SEBAB (3-IN-1 BOX) ---
with st.container(border=True):
    st.markdown("### Tafsir Sebab")
    cols = st.columns(3)
    for i, idx in enumerate(sebab_indices):
        with cols[i]:
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.markdown(f"**{d[0]} {d[1]}:{d[2]}**")
                st.write(d[3])
            else:
                st.caption(f"Index {idx}: Log Kosong")

st.write("")

# --- 6. BOX TAFSIR PERBAIKAN (3-IN-1 BOX) ---
with st.container(border=True):
    st.markdown("### Tafsir Perbaikan")
    cols = st.columns(3)
    for i, idx in enumerate(perbaikan_indices):
        with cols[i]:
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.markdown(f"**{d[0]} {d[1]}:{d[2]}**")
                st.write(d[3])
            else:
                st.caption(f"Index {idx}: Log Kosong")

st.markdown("---")
st.caption(f"Operator Mode | Sistem Terverifikasi | {datetime.now().strftime('%Y')}")

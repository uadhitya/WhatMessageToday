import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE (LOGIKA TETAP) ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    DATA_YAWM = {}

# --- 2. LOGIKA INDEKS (LOGIKA TETAP) ---
def get_indices(n):
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    perbaikan = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, perbaikan

# --- 3. ANTARMUKA & PENYEMPURNAAN DESIGN ---
st.set_page_config(page_title="WhatMessageToday | Audit System", layout="wide")

# Custom CSS untuk meningkatkan estetika "Operator System"
st.markdown("""
    <style>
    /* Mengatur latar belakang dan font */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Styling Header Utama */
    .main-header {
        font-size: 3rem !important;
        font-weight: 800;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    
    /* Styling Card/Box agar lebih modern */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #31333F !important;
        border-radius: 12px !important;
        background-color: #161b22 !important;
        transition: transform 0.2s ease;
    }
    
    /* Indeks Highlight */
    .index-label {
        color: #8b949e;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .data-header {
        color: #58a6ff;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    /* Highlight untuk Tafsir Sebab dan Perbaikan */
    .section-title {
        border-left: 4px solid #f85149; /* Merah untuk sebab */
        padding-left: 15px;
        margin-bottom: 20px;
    }
    .section-title-alt {
        border-left: 4px solid #3fb950; /* Hijau untuk perbaikan */
        padding-left: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-header">WHAT MESSAGE TODAY</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>System Operator Interface | Internal Audit Mode</p>", unsafe_allow_html=True)

# Area Input (Dibuat lebih ringkas)
col_input1, col_input2, col_input3 = st.columns([1, 1, 1])
with col_input2:
    target_date = st.date_input("📅 Tentukan Periode Audit", value=datetime.now(),
                                min_value=datetime(1900, 1, 1),
                                max_value=datetime(2200, 12, 31))

day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
sebab_indices, perbaikan_indices = get_indices(n)

st.write("")

# --- 4. PUSAT AUDIT (DAY X) ---
# Menggunakan container untuk fokus utama
with st.container(border=True):
    if n in DATA_YAWM:
        d = DATA_YAWM[n]
        st.markdown(f"<p class='index-label'>AUDIT POINT INDEX {n}</p>", unsafe_allow_html=True)
        st.markdown(f"## Day {n} Tahun Ini")
        st.info(f"**{d[0]} {d[1]}:{d[2]}**")
        st.markdown(f"*{d[3]}*")
    else:
        st.warning(f"Index {n} | Data belum terintegrasi dalam sistem.")

st.write("")

# --- 5. TAFSIR SEBAB & PERBAIKAN (SIDE BY SIDE) ---
col_sebab, col_perbaikan = st.columns(2)

with col_sebab:
    st.markdown('<div class="section-title"><h3>Tafsir Sebab (-120, -80, -40)</h3></div>', unsafe_allow_html=True)
    for i, idx in enumerate(sebab_indices):
        labels = ["Index -120", "Index -80", "Index -40"]
        with st.container(border=True):
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.markdown(f"<span class='index-label'>{labels[i]} | {idx}</span>", unsafe_allow_html=True)
                st.markdown(f"<p class='data-header'>{d[0]} {d[1]}:{d[2]}</p>", unsafe_allow_html=True)
                st.write(d[3])
            else:
                st.caption(f"{labels[i]} | {idx} (No Data)")

with col_perbaikan:
    st.markdown('<div class="section-title-alt"><h3>Tafsir Perbaikan (+40, +80, +120)</h3></div>', unsafe_allow_html=True)
    for i, idx in enumerate(perbaikan_indices):
        labels = ["Index +40", "Index +80", "Index +120"]
        with st.container(border=True):
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.markdown(f"<span class='index-label'>{labels[i]} | {idx}</span>", unsafe_allow_html=True)
                st.markdown(f"<p class='data-header' style='color:#3fb950'>{d[0]} {d[1]}:{d[2]}</p>", unsafe_allow_html=True)
                st.write(d[3])
            else:
                st.caption(f"{labels[i]} | {idx} (No Data)")

st.markdown("---")
st.caption(f"Operator Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

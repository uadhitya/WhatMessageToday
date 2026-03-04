import streamlit as st
from datetime import datetime

# --- 1. LOGIKA INTI (TIDAK BOLEH BERUBAH) ---
try:
    from database_yawm import DATA_YAWM
except:
    DATA_YAWM = {}

def get_indices(n):
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    perbaikan = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, perbaikan

# --- 2. KREASI VISUAL (INDUSTRIAL DASHBOARD) ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")
st.markdown("""
    <style>
    /* Latar Belakang & Font Base */
    .stApp { background-color: #0b0e14; color: #c9d1d9; }
    
    /* Header Container */
    .header-container {
        background: linear-gradient(90deg, #161b22 0%, #0b0e14 100%);
        padding: 30px;
        border-radius: 0 0 15px 15px;
        border-bottom: 2px solid #3b82f6;
        margin-bottom: 40px;
    }
    .day-num { color: #ffffff; font-size: 4rem; font-weight: 900; line-height: 1; text-shadow: 2px 2px #000; }
    .year-tag { color: #3b82f6; font-size: 1.2rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; }

    /* Card Styling */
    .glass-card {
        background: rgba(22, 27, 34, 0.8);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 25px;
        transition: transform 0.2s, border 0.2s;
    }
    .glass-card:hover { border-color: #3b82f6; }

    /* Typography */
    .ref-label { 
        color: #f59e0b; /* Amber untuk Identitas */
        font-family: 'Courier New', monospace;
        font-weight: 700; 
        font-size: 0.9rem; 
        margin-bottom: 12px;
        display: block;
    }
    .message-body { 
        color: #e6edf3; 
        font-size: 1.3rem; 
        line-height: 1.6; 
        font-weight: 400;
    }
    
    /* Section Labels */
    .status-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 15px;
    }
    .tag-sebab { background-color: #442a2a; color: #ff7b72; border: 1px solid #6e3636; }
    .tag-perbaikan { background-color: #233329; color: #7ee787; border: 1px solid #2ea043; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INPUT (PARAMETER HARGA MATI) ---
# Saya tetap mengunci 1900-2200 di sini.
target_date = st.date_input(
    "OPERATIONAL DATE AUDIT", 
    value=datetime.now(),
    min_value=datetime(1900, 1, 1),
    max_value=datetime(2200, 12, 31)
)

day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
tahun_audit = target_date.year
sebab_idx, perbaikan_idx = get_indices(n)

# --- 4. RENDER HEADER ---
st.markdown(f"""
    <div class='header-container'>
        <div class='year-tag'>System Chronology {tahun_audit}</div>
        <div class='day-num'>DAY {n}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. RENDER DATA UTAMA ---
if n in DATA_YAWM:
    d = DATA_YAWM[n]
    st.markdown(f"""
        <div class='glass-card' style='border-left: 5px solid #3b82f6;'>
            <span class='ref-label'>ID: {d[0]} {d[1]}:{d[2]}</span>
            <div class='message-body'>{d[-1]}</div>
        </div>
        """, unsafe_allow_html=True)

# --- 6. TAFSIR DENGAN AKSI WARNA ---
st.write("")
col_sebab, col_perbaikan = st.columns(2)

with col_sebab:
    st.markdown("<div class='status-tag tag-sebab'>Tafsir Sebab (-120, -80, -40)</div>", unsafe_allow_html=True)
    for idx in sebab_idx:
        if idx in DATA_YAWM:
            v = DATA_YAWM[idx]
            st.markdown(f"""
                <div class='glass-card' style='margin-bottom:10px;'>
                    <span class='ref-label'>{v[0]} {v[1]}:{v[2]}</span>
                    <div class='message-body' style='font-size:1rem;'>{v[-1]}</div>
                </div>
                """, unsafe_allow_html=True)

with col_perbaikan:
    st.markdown("<div class='status-tag tag-perbaikan'>Tafsir Perbaikan (+40, +80, +120)</div>", unsafe_allow_html=True)
    for idx in perbaikan_idx:
        if idx in DATA_YAWM:
            v = DATA_YAWM[idx]
            st.markdown(f"""
                <div class='glass-card' style='margin-bottom:10px;'>
                    <span class='ref-label'>{v[0]} {v[1]}:{v[2]}</span>
                    <div class='message-body' style='font-size:1rem;'>{v[-1]}</div>
                </div>
                """, unsafe_allow_html=True)

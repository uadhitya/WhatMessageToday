import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE (Integritas Data 365) ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    # Jika file belum ada, sistem tetap berjalan tanpa crash
    DATA_YAWM = {}

# --- 2. LOGIKA INDEKS (Sistem Mutlak) ---
def get_indices(n):
    # Logika sirkular untuk mencari Sebab (-120, -80, -40) dan Perbaikan (+40, +80, +120)
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    perbaikan = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, perbaikan

# --- 3. UI CONFIG & AUDIT VISUAL ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")

# CSS untuk mendukung Teks Arab (RTL) dan tipografi yang presisi
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .arabic { font-family: 'Amiri', serif; direction: rtl; text-align: right; font-size: 1.8rem; line-height: 2.2; margin-bottom: 10px; }
    .latin { font-style: italic; color: #9ca3af; font-size: 1rem; line-height: 1.6; }
    .identitas { font-weight: bold; color: #3b82f6; font-size: 1.1rem; }
    /* Border untuk Container Tafsir */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #30363d !important;
        background-color: #161b22 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# WhatMessageToday")

# --- 4. KONTROL WAKTU (RESTORASI PARAMETER 1900-2200) ---
# Saya mengunci kembali rentang waktu yang sebelumnya saya hilangkan.
target_date = st.date_input(
    "Audit Period", 
    value=datetime.now(),
    min_value=datetime(1900, 1, 1),
    max_value=datetime(2200, 12, 31)
)

# Menghitung Day of Year (n)
day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
sebab_indices, perbaikan_indices = get_indices(n)

# --- 5. TITIK PUSAT (DAY N) ---
if n in DATA_YAWM:
    d = DATA_YAWM[n]
    st.markdown(f"## Day {n} Tahun Ini")
    st.markdown(f"<p class='identitas'>{d[0]} {d[1]}:{d[2]}</p>", unsafe_allow_html=True)
    
    # Cek jika database memiliki 5 elemen (termasuk Arab)
    if len(d) >= 5:
        st.markdown(f"<p class='arabic'>{d[3]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='latin'>{d[4]}</p>", unsafe_allow_html=True)
    else:
        # Fallback jika hanya ada teks pesan (4 elemen)
        st.markdown(f"<p class='latin'>{d[3]}</p>", unsafe_allow_html=True)
else:
    st.info(f"Data untuk Day {n} belum terinput dalam database.")

st.write("") # Spacer

# --- 6. BOX TAFSIR (SEBAB & PERBAIKAN) ---
# Menggunakan kolom 3-in-1 untuk efisiensi pandangan operator
for title, indices in [("Tafsir Sebab", sebab_indices), ("Tafsir Perbaikan", perbaikan_indices)]:
    with st.container(border=True):
        st.markdown(f"### {title}")
        cols = st.columns(3)
        for i, idx in enumerate(indices):
            with cols[i]:
                if idx in DATA_YAWM:
                    item = DATA_YAWM[idx]
                    st.markdown(f"<p class='identitas'>{item[0]} {item[1]}:{item[2]}</p>", unsafe_allow_html=True)
                    if len(item) >= 5:
                        st.markdown(f"<p class='arabic' style='font-size:1.3rem;'>{item[3]}</p>", unsafe_allow_html=True)
                        st.markdown(f"<p class='latin'>{item[4]}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p class='latin'>{item[3]}</p>", unsafe_allow_html=True)
                else:
                    st.caption(f"Index {idx} Kosong")

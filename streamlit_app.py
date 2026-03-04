import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    DATA_YAWM = {}

# --- 2. LOGIKA INDEKS ---
def get_indices(n):
    sebab = [((n - d - 1) % 365) + 1 for d in [120, 80, 40]]
    perbaikan = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return sebab, perbaikan

# --- 3. ANTARMUKA WHATMESSAGETODAY ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")
st.markdown("# WhatMessageToday")

target_date = st.date_input("Audit Period", value=datetime.now(),
                            min_value=datetime(1900, 1, 1),
                            max_value=datetime(2200, 12, 31))

day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
sebab_indices, perbaikan_indices = get_indices(n)

st.write("---")

# --- 4. PENEGASAN HASIL DAY X (TITIK PUSAT) ---
if n in DATA_YAWM:
    d = DATA_YAWM[n]
    st.markdown(f"## Day {n} Tahun Ini | Index {n}")
    st.markdown(f"### {d[0]} {d[1]}:{d[2]}")
    st.markdown(d[3])
else:
    st.write(f"Day {n} | Index {n}")
    st.write("Data belum diinput")

st.write("---")

# --- 5. BOX TAFSIR SEBAB (-120, -80, -40) ---
with st.container(border=True):
    st.markdown("### Tafsir Sebab")
    cols = st.columns(3)
    labels = ["Index -120", "Index -80", "Index -40"]
    for i, idx in enumerate(sebab_indices):
        with cols[i]:
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.write(f"{labels[i]} | {idx}")
                st.write(f"**{d[0]} {d[1]}:{d[2]}**")
                st.write(d[3])
            else:
                st.write(f"{labels[i]} | {idx}")
                st.write("Data belum diinput")

st.write("---")

# --- 6. BOX TAFSIR PERBAIKAN (+40, +80, +120) ---
with st.container(border=True):
    st.markdown("### Tafsir Perbaikan")
    cols = st.columns(3)
    labels = ["Index +40", "Index +80", "Index +120"]
    for i, idx in enumerate(perbaikan_indices):
        with cols[i]:
            if idx in DATA_YAWM:
                d = DATA_YAWM[idx]
                st.write(f"{labels[i]} | {idx}")
                st.write(f"**{d[0]} {d[1]}:{d[2]}**")
                st.write(d[3])
            else:
                st.write(f"{labels[i]} | {idx}")
                st.write("Data belum diinput")

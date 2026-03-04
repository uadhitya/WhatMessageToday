import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    st.error("File 'database_yawm.py' tidak ditemukan.")
    DATA_YAWM = {}

# --- 2. LOGIKA MATRIKS 3-LANGKAH ---
def get_full_matrix(n):
    # Masa Lalu (Retro)
    past = [((n - d - 1) % 365) + 1 for d in [40, 80, 120]]
    # Masa Depan (Future)
    future = [((n + d - 1) % 365) + 1 for d in [40, 80, 120]]
    return past, future

# --- 3. ANTARMUKA CLEAN LOOK ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")
st.title("🛡️ WhatMessageToday: Operator Dashboard")

target_date = st.date_input(
    "Audit Period", 
    value=datetime.now(),
    min_value=datetime(1900, 1, 1),
    max_value=datetime(2200, 12, 31)
)

# Konversi Indeks
day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year
past_indices, future_indices = get_full_matrix(n)

st.divider()

# --- 4. RENDER UTAMA (STATUS HARI INI) ---
if n in DATA_YAWM:
    data = DATA_YAWM[n]
    st.info(f"📍 **STATUS UTAMA (Day {n} Tahun Ini)**")
    st.subheader(f"{data[0]} {data[1]}:{data[2]}")
    st.write(f"**{data[3]}**")
else:
    st.warning(f"Data Day {n} belum tersedia.")

st.divider()

# --- 5. GABUNGAN INDEX MASA LALU (-40, -80, -120) ---
st.markdown("### 🔍 Audit Masa Lalu (Akar -40, -80, -120)")
cols_past = st.columns(3)
labels_past = ["Akar (-40d)", "Inkubasi (-80d)", "Benih (-120d)"]

for i, idx in enumerate(past_indices):
    with cols_past[i]:
        if idx in DATA_YAWM:
            d = DATA_YAWM[idx]
            st.caption(f"{labels_past[i]} | Index {idx}")
            st.markdown(f"**{d[0]} {d[1]}:{d[2]}**")
            st.write(f"*{d[3]}*")
        else:
            st.caption(f"Index {idx}")
            st.write("Data Pending")

st.divider()

# --- 6. GABUNGAN INDEX MASA DEPAN (+40, +80, +120) ---
st.markdown("### 🚀 Proyeksi Masa Depan (Dampak +40, +80, +120)")
cols_future = st.columns(3)
labels_future = ["Reaksi (+40d)", "Stabilisasi (+80d)", "Outcome (+120d)"]

for i, idx in enumerate(future_indices):
    with cols_future[i]:
        if idx in DATA_YAWM:
            d = DATA_YAWM[idx]
            st.caption(f"{labels_future[i]} | Index {idx}")
            st.markdown(f"**{d[0]} {d[1]}:{d[2]}**")
            st.write(f"*{d[3]}*")
        else:
            st.caption(f"Index {idx}")
            st.write("Data Pending")

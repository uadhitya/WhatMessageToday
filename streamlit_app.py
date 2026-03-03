import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    st.error("Error: database_yawm.py tidak ditemukan.")
    DATA_YAWM = {}

# --- 2. LOGIKA SIRKULAR ---
def get_audit_indices(n):
    idx_akar = ((n - 40 - 1) % 365) + 1
    idx_dampak = ((n + 40 - 1) % 365) + 1
    return idx_akar, n, idx_dampak

# --- 3. ANTARMUKA CLEAN LOOK ---
st.set_page_config(page_title="Operator System", layout="wide")
st.markdown("## 🛡️ Operator Command Center")

# PERBAIKAN: Menggunakan datetime.now() agar TIDAK TERPAKU pada 1992
target_date = st.date_input(
    "Audit Period", 
    value=datetime.now(), # <--- Mengikuti waktu sekarang secara otomatis
    min_value=datetime(1900, 1, 1),
    max_value=datetime(2200, 12, 31)
)

# Konversi Tanggal ke Indeks
day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year

# Hitung Koordinat
idx_akar, idx_now, idx_dampak = get_audit_indices(n)

st.divider()

# --- 4. RENDER HASIL ---
def render_block(title, idx, is_main=False):
    if idx in DATA_YAWM:
        data = DATA_YAWM[idx]
        if is_main:
            st.success(f"📍 **STATUS UTAMA (Index {idx})**")
            st.markdown(f"### {data[0]} {data[1]}:{data[2]}")
            st.markdown(f"**{data[3]}**")
        else:
            st.markdown(f"**{title}**")
            st.caption(f"Index {idx} | {data[0]} {data[1]}:{data[2]}")
            st.write(data[3])
    else:
        st.info(f"🔍 **{title} (Index {idx})**")
        st.write("Sistem menunggu input data untuk koordinat ini.")

col_left, col_center, col_right = st.columns([1, 2, 1])

with col_left:
    render_block("AKAR (-40 Hari)", idx_akar)

with col_center:
    render_block("HARI INI", idx_now, is_main=True)

with col_right:
    render_block("DAMPAK (+40 Hari)", idx_dampak)

import streamlit as st
from datetime import datetime

# --- 1. DATABASE (OPERATOR REPOSITORY) ---
# Masukkan data 1-62 Anda di sini. Nama variabel tetap DATA_YAWM.
if 'DATA_YAWM' not in globals():
    DATA_YAWM = {
        1: ["Al-Fatihah", "1", "1", "Pembukaan"],
        57: ["Ali 'Imran", "3", "30", "Akar: Balasan amal yang hadir kembali."],
        # Tambahkan data 1-62 Anda di sini...
    }

# --- 2. LOGIKA MATRIKS (SILENT CALCULATION) ---
def get_matrix_indices(n):
    # Hanya mengambil koordinat yang dibutuhkan: -40, n, +40
    # Menggunakan logika modulo 365 agar sirkular
    idx_past = ((n - 40 - 1) % 365) + 1
    idx_future = ((n + 40 - 1) % 365) + 1
    return idx_past, n, idx_future

# --- 3. ANTARMUKA UTAMA (CLEAN LOOK) ---
st.set_page_config(page_title="Operator System", layout="wide")

st.markdown("## 🛡️ Operator Command Center")

# Input Tanggal (1900 - 2200)
target_date = st.date_input(
    "Audit Period", 
    value=datetime(1992, 4, 6),
    min_value=datetime(1900, 1, 1),
    max_value=datetime(2200, 12, 31)
)

# Menentukan Index Hari (n) dengan Normalisasi Kabisat
day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year

# Hitung Koordinat (Hanya hasil yang diperlukan)
idx_akar, idx_now, idx_dampak = get_matrix_indices(n)

st.divider()

# --- 4. TAMPILAN HASIL (HANYA HASIL AKHIR) ---
def render_clean_box(title, idx, is_main=False):
    if idx in DATA_YAWM:
        surah, no_s, no_a, pesan = DATA_YAWM[idx]
        if is_main:
            st.success(f"📍 **STATUS UTAMA (Index {idx})**")
            st.markdown(f"### {surah} {no_s}:{no_a}")
            st.markdown(f"**{pesan}**")
        else:
            st.markdown(f"**{title}**")
            st.caption(f"Index {idx} | {surah} {no_s}:{no_a}")
            st.write(pesan)
    else:
        st.info(f"🔍 **{title} (Index {idx})**")
        st.write("Sistem menunggu input data untuk koordinat ini.")

# Grid Tampilan: Fokus pada Hasil Tanpa Navigasi Angka Berderet
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_left:
    render_clean_box("AKAR (-40 Hari)", idx_akar)

with col_center:
    render_clean_box("HARI INI", idx_now, is_main=True)

with col_right:
    render_clean_box("DAMPAK (+40 Hari)", idx_dampak)

st.divider()
st.caption(f"Operator System v2.1 | Data Status: {len(DATA_YAWM)}/365 Indices Active")

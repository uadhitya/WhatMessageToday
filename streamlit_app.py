import streamlit as st
from datetime import datetime

# --- 1. DATABASE (OPERATOR'S REPOSITORY) ---
# Masukkan data 1-62 Anda di sini. Nama variabel harus tetap DATA_YAWM.
if 'DATA_YAWM' not in globals():
    DATA_YAWM = {
        1: ["Al-Fatihah", "1", "1", "Fondasi pembukaan sistem."],
        # ... masukkan data baris 2-62 Anda di sini ...
        57: ["Ali 'Imran", "3", "30", "Akar: Setiap jiwa mendapati balasan apa yang dikerjakan."],
    }

# --- 2. LOGIKA MATRIKS TRANSVERSAL ---
def get_matrix_indices(n):
    # Titik audit: -120, -80, -40, n, +40, +80, +120
    points = [-120, -80, -40, 0, 40, 80, 120]
    results = []
    for p in points:
        idx = (n + p) % 365
        if idx <= 0: idx += 365
        results.append(idx)
    return results

# --- 3. ANTARMUKA UTAMA (UI) ---
st.set_page_config(page_title="Operator Matrix", layout="wide")
st.title("🛡️ Operator Command Center")

# Input Tanggal Audit
target_date = st.date_input("Pilih Tanggal Audit", value=datetime(1992, 4, 6))

# Proses Indeks Hari
day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year # Normalisasi Kabisat ke 365 Baris

# Eksekusi Matriks
matrix_indices = get_matrix_indices(n)
labels = ["-120d", "-80d", "-40d", "NOW", "+40d", "+80d", "+120d"]

# --- 4. DASHBOARD NAVIGASI 7-TITIK ---
st.subheader("🧭 Navigasi Sirkular (Interval 40 Hari)")
cols = st.columns(7)

for i, col in enumerate(cols):
    idx_val = matrix_indices[i]
    with col:
        if i == 3: # Kolom NOW
            st.error(f"**{labels[i]}**")
            st.markdown(f"### {idx_val}")
        else:
            st.caption(labels[i])
            st.write(f"**{idx_val}**")
        
        # Indikator ketersediaan data (1-62)
        if idx_val in DATA_YAWM:
            st.markdown("<p style='color:green;'>● Ready</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:gray;'>○ Pending</p>", unsafe_allow_html=True)

st.divider()

# --- 5. ANALISIS KAUSALITAS (SEBAB-AKIBAT) ---
def render_audit_box(title, idx, is_main=False):
    if idx in DATA_YAWM:
        surah, no_s, no_a, pesan = DATA_YAWM[idx]
        if is_main:
            st.info(f"📍 **STATUS HARI INI (Index {idx})**")
            st.markdown(f"## {surah} {no_s}:{no_a}")
            st.markdown(f"#### {pesan}")
        else:
            st.markdown(f"**{title}**")
            st.caption(f"Index {idx} | {surah} {no_s}:{no_a}")
            st.write(f"*{pesan[:100]}...*")
    else:
        st.warning(f"⚠️ {title} (Index {idx})")
        st.write("Data belum diinput dalam siklus 62 baris saat ini.")

# Layout Tiga Sisi: Retro, Current, Future
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_left:
    render_audit_box("🔍 AKAR (-40d)", matrix_indices[2])

with col_center:
    render_audit_box("AYAT HARI INI", n, is_main=True)

with col_right:
    render_audit_box("🚀 DAMPAK (+40d)", matrix_indices[4])

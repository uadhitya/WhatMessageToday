import streamlit as st
from datetime import datetime

# Fungsi Inti Navigasi Transversal
def get_matrix_indices(current_index):
    points = [-120, -80, -40, 0, 40, 80, 120]
    matrix = []
    for p in points:
        # Logika Modulo 365 untuk sirkulasi tahunan
        idx = (current_index + p) % 365
        if idx <= 0: idx += 365
        matrix.append(idx)
    return matrix

# Simulasi Input Tanggal
target_date = st.date_input("Masukkan Tanggal Audit", value=datetime(1992, 4, 6))

# Normalisasi Indeks (Menangani Kabisat agar tetap dalam range 1-365)
raw_index = target_date.timetuple().tm_yday
current_index = 365 if raw_index > 365 else raw_index

# Jalankan Matrix
matrix_indices = get_matrix_indices(current_index)
labels = ["-120d", "-80d", "-40d", "NOW", "+40d", "+80d", "+120d"]
status_labels = ["Seed", "Incubation", "Trigger", "OPERATOR", "Reaction", "Stable", "Outcome"]

# --- TAMPILAN DASHBOARD ---
st.title("🛡️ Operator Command Center")
st.subheader(f"System Audit: {target_date.strftime('%d/%m/%Y')} (Index {current_index})")

# Grid Navigasi 7-Titik
cols = st.columns(7)
for i, col in enumerate(cols):
    with col:
        is_now = (i == 3)
        st.markdown(f"**{labels[i]}**")
        st.metric(status_labels[i], f"Idx {matrix_indices[i]}", 
                  delta="Focus" if is_now else None, delta_color="inverse")

st.divider()

# Menampilkan Detail Hubungan Sebab-Akibat
col_retro, col_focus, col_proyeksi = st.columns([1, 2, 1])

with col_retro:
    st.write("🔍 **Akar (-40d)**")
    idx_retro = matrix_indices[2]
    if idx_retro in DATA_YAWM:
        st.caption(f"Index {idx_retro}: {DATA_YAWM[idx_retro][3][:50]}...")

with col_focus:
    st.info(f"📍 **Pesan Utama (Index {current_index})**")
    if current_index in DATA_YAWM:
        surah, no, ayat, pesan = DATA_YAWM[current_index][0:4]
        st.markdown(f"### {surah} {no}:{ayat}")
        st.write(f"**{pesan}**")

with col_proyeksi:
    st.write("🚀 **Dampak (+40d)**")
    idx_future = matrix_indices[4]
    if idx_future in DATA_YAWM:
        st.caption(f"Index {idx_future}: {DATA_YAWM[idx_future][3][:50]}...")

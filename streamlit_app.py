import streamlit as st
import datetime
from database_yawm import DATA_YAWM

# 1. Konfigurasi Halaman
st.set_page_config(page_title="What Message Today", page_icon="📖", layout="centered")

st.title("📖 What Message Today")
st.write("Sistem Pemetaan Waktu ke Pesan Al-Qur'an")

# 2. Pengaturan Rentang Kalender
min_date = datetime.date(1990, 1, 1)
max_date = datetime.date(2200, 12, 31)
today = datetime.date.today()
default_date = today if min_date <= today <= max_date else min_date

target_date = st.date_input(
    "Pilih Tanggal Operasi:", 
    value=default_date,
    min_value=min_date,
    max_value=max_date,
    format="DD/MM/YYYY"
)

# 3. Logika Perhitungan (Kumulatif & Tahunan)
start_date = datetime.date(1990, 1, 1)
hari_ke_akumulatif = (target_date - start_date).days + 1

# Menghitung hari ke-x di tahun berjalan (misal: 1 - 365/366)
awal_tahun = datetime.date(target_date.year, 1, 1)
hari_ke_tahunan = (target_date - awal_tahun).days + 1

# Indeks tetap menggunakan modulo 365 untuk sinkronisasi database
indeks = hari_ke_akumulatif % 365
if indeks == 0: indeks = 365

st.divider()

# 4. Tampilan Metrik (Ditambah konteks tahunan)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Hari Ke- (Total)", f"{hari_ke_akumulatif:,}")
with col2:
    # Menampilkan posisi hari dalam tahun yang dipilih
    st.metric(f"Hari di {target_date.year}", hari_ke_tahunan)
with col3:
    st.metric("Index Yawm", indeks)

# 5. Output Pesan
st.subheader(f"📅 Hasil Sinkronisasi: {target_date.strftime('%d %B %Y')}")

if indeks in DATA_YAWM:
    surah, no, ayat, pesan = DATA_YAWM[indeks]
    st.info(f"📍 **Surah {surah} (Ayat {no}:{ayat})**")
    st.markdown(f"""
        <div style="background-color: #1e2130; padding: 25px; border-left: 8px solid #ff4b4b; border-radius: 10px; margin-top: 10px;">
            <h2 style="color: white; font-family: 'serif'; font-style: italic; line-height: 1.5;">
                "{pesan}"
            </h2>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption(f"Operator Mode: Active | Memetakan Hari ke-{hari_ke_tahunan} pada tahun {target_date.year}")

import streamlit as st
import datetime
from database_yawm import DATA_YAWM

# 1. Konfigurasi Halaman
st.set_page_config(page_title="What Message Today", page_icon="📖", layout="centered")

st.title("📖 What Message Today")
st.write("Sistem Pemetaan Waktu Universal (1900 - 2200)")

# 2. Pengaturan Rentang Kalender Luas (Mendukung tahun 1945)
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2200, 12, 31)
today = datetime.date.today()

target_date = st.date_input(
    "Pilih Tanggal Lahir atau Peristiwa:", 
    value=today,
    min_value=min_date,
    max_value=max_date,
    format="DD/MM/YYYY"
)

# 3. LOGIKA KONSISTEN: Mengambil urutan hari dalam tahun (1-366)
# Ini memastikan 17 Agustus 1945 dan 17 Agustus 2026 punya basis pesan yang sinkron
indeks = target_date.timetuple().tm_yday

# Penyesuaian untuk database yang hanya 365 hari (menangani hari ke-366/kabisat)
indeks_pesan = indeks
if indeks_pesan > 365:
    indeks_pesan = 365

st.divider()

# 4. Tampilan Metrik
col1, col2 = st.columns(2)
with col1:
    st.metric(f"Hari ke- (di tahun {target_date.year})", indeks)
with col2:
    st.metric("Index Pesan", indeks_pesan)

# 5. Output Pesan Al-Qur'an
st.subheader(f"📅 Peristiwa: {target_date.strftime('%d %B %Y')}")

if indeks_pesan in DATA_YAWM:
    data = DATA_YAWM[indeks_pesan]
    surah, no, ayat, pesan = data[0], data[1], data[2], data[3]
    
    st.info(f"📍 **Surah {surah} ({no}:{ayat})**")
    
    # Tampilan Arab (Jika ada di database)
    if len(data) > 4:
        st.markdown(f"<div style='direction: rtl; text-align: right; font-size: 28px; padding: 10px;'>{data[4]}</div>", unsafe_allow_html=True)

    # Box Intisari Pesan
    st.markdown(f"""
        <div style="background-color: #1e2130; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 8px;">
            <p style="color: white; font-style: italic; font-size: 18px; margin: 0;">"{pesan}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Terjemahan Lengkap (Jika ada)
    if len(data) > 5:
        st.write(f"**Terjemahan:** {data[5]}")
else:
    st.warning(f"Data Indeks {indeks_pesan} belum tersedia.")

st.divider()
st.caption("Operator: Active | Sistem Sinkronisasi Kalender Tahunan")

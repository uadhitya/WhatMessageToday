import streamlit as st
import datetime
from database_yawm import DATA_YAWM

# 1. Konfigurasi
st.set_page_config(page_title="What Message Today", page_icon="📖")

st.title("📖 What Message Today")
st.write("Sistem Pemetaan Waktu: Sinkronisasi Tahunan")

# 2. Input Tanggal
target_date = st.date_input("Pilih Tanggal:", datetime.date.today(), format="DD/MM/YYYY")

# 3. LOGIKA PEMBENAHAN: Sinkronisasi Hari ke-X dalam Tahun
# Menghitung hari ke berapa tanggal tersebut dalam tahun yang dipilih
awal_tahun = datetime.date(target_date.year, 1, 1)
hari_ke_tahunan = (target_date - awal_tahun).days + 1

# Index Yawm sekarang mengikuti hari ke-x dalam tahun tersebut
# Jika hari ke-366 (Kabisat), kita arahkan kembali ke 365 atau pesan khusus
indeks = hari_ke_tahunan
if indeks > 365: indeks = 365 

st.divider()

# 4. Dashboard Metrik
c1, c2 = st.columns(2)
with c1:
    st.metric(f"Hari di {target_date.year}", hari_ke_tahunan)
with c2:
    st.metric("Index Pesan", indeks)

# 5. Penampilan Pesan Berdasarkan Indeks Tahunan
if indeks in DATA_YAWM:
    data = DATA_YAWM[indeks]
    surah, no, ayat, pesan = data[0], data[1], data[2], data[3]
    
    st.subheader(f"📅 {target_date.strftime('%d %B %Y')}")
    st.markdown(f"### 📍 {surah} ({no}:{ayat})")
    
    # Tampilkan Arab (Jika ada)
    if len(data) > 4:
        st.markdown(f"<div style='direction: rtl; text-align: right; font-size: 28px;'>{data[4]}</div>", unsafe_allow_html=True)

    # Box Pesan
    st.info(f'"{pesan}"')
    
    # Terjemahan (Jika ada)
    if len(data) > 5:
        st.write(data[5])
else:
    st.error(f"Data untuk hari ke-{indeks} belum tersedia di database.")

st.divider()
st.caption("Sistem Konsisten: Pesan mengikuti urutan hari tahunan (1-365).")

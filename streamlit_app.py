import streamlit as st
import datetime
from database_yawm import DATA_YAWM

# Konfigurasi Tampilan
st.set_page_config(page_title="What Message Today", page_icon="📖")

st.title("📖 What Message Today")
st.write("Sistem Pemetaan Waktu Linear ke Pesan Al-Qur'an (1990 - 2200)")

# Input Tanggal via Kalender
target_date = st.date_input("Pilih Tanggal:", datetime.date.today())

# Logika Perhitungan
start_date = datetime.date(1990, 1, 1)

if target_date < start_date or target_date > datetime.date(2200, 12, 31):
    st.error("Maaf, tanggal di luar jangkauan sistem (1990 - 2200)")
else:
    # Hitung Hari
    hari_ke = (target_date - start_date).days + 1
    indeks = hari_ke % 365
    if indeks == 0: indeks = 365

    # Tampilan Output
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Hari Ke-", hari_ke)
    with col2:
        st.metric("Index Yawm", indeks)

    st.subheader(f"📅 Sinkronisasi: {target_date.strftime('%d %B %Y')}")
    
    # Ambil Data dari database_yawm.py
    if indeks in DATA_YAWM:
        surah, no, ayat, pesan = DATA_YAWM[indeks]
        st.info(f"**Surah {surah} ({no}:{ayat})**")
        st.markdown(f"### *\"{pesan}\"*")
    else:
        st.warning(f"Message untuk Index {indeks} belum tersinkronisasi di database.")

st.divider()
st.caption("What Message Today System | Operator Mode: Active")

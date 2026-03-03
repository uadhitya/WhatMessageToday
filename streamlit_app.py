import streamlit as st
import datetime
from database_yawm import DATA_YAWM

# 1. Konfigurasi Halaman
st.set_page_config(page_title="What Message Today", page_icon="📖", layout="centered")

# 2. Judul & Header
st.title("📖 What Message Today")
st.write("Sistem Pemetaan Waktu Mandiri")

# 3. Input Tanggal (1990 - 2200)
min_date, max_date = datetime.date(1990, 1, 1), datetime.date(2200, 12, 31)
target_date = st.date_input("Pilih Tanggal:", datetime.date.today(), min_value=min_date, max_value=max_date, format="DD/MM/YYYY")

# 4. Logika Perhitungan
hari_ke_total = (target_date - min_date).days + 1
hari_ke_tahunan = (target_date - datetime.date(target_date.year, 1, 1)).days + 1
indeks = hari_ke_total % 365 or 365

st.divider()

# 5. Dashboard Metrik
c1, c2, c3 = st.columns(3)
c1.metric("Total Hari", f"{hari_ke_total:,}")
c2.metric(f"Hari di {target_date.year}", hari_ke_tahunan)
c3.metric("Index Yawm", indeks)

# 6. Penampilan Data Qur'an
if indeks in DATA_YAWM:
    # Mengantisipasi jika nanti Anda menambah kolom di database_yawm.py
    data = DATA_YAWM[indeks]
    surah, no, ayat, pesan = data[0], data[1], data[2], data[3]
    
    st.subheader(f"📅 {target_date.strftime('%d %B %Y')}")
    
    # Header Surah & Ayat
    st.markdown(f"### 📍 {surah} ({no}:{ayat})")
    
    # Slot untuk Teks Arab (Jika sudah Anda tambahkan di database)
    if len(data) > 4:
        st.markdown(f"<p style='text-align: right; font-size: 28px; font-family: sans-serif;'>{data[4]}</p>", unsafe_allow_html=True)

    # Box Pesan Intisari (Visual yang sudah diperkecil)
    st.markdown(f"""
        <div style="background-color: #1e2130; padding: 15px; border-left: 5px solid #ff4b4b; border-radius: 8px;">
            <p style="color: white; font-style: italic; font-size: 18px; margin: 0;">"{pesan}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Slot untuk Terjemahan Lengkap (Jika sudah Anda tambahkan di database)
    if len(data) > 5:
        st.caption(f"**Terjemahan:** {data[5]}")

st.divider()
st.caption("Operator Mode: Active | Standalone Database System")

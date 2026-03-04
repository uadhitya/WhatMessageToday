import streamlit as st
from datetime import datetime

# --- 1. KONEKSI DATABASE ---
try:
    from database_yawm import DATA_YAWM
except ImportError:
    DATA_YAWM = {}

# --- 2. LOGIKA TRANSVERSAL (Modulo 365) ---
def get_chronological_indices(n):
    # Urutan linear: -120, -80, -40, 0, 40, 80, 120
    steps = [-120, -80, -40, 0, 40, 80, 120]
    return [((n + s - 1) % 365) + 1 for s in steps]

# --- 3. ANTARMUKA WHATMESSAGETODAY ---
st.set_page_config(page_title="WhatMessageToday", layout="wide")
st.markdown("WhatMessageToday")

target_date = st.date_input("Audit Period", value=datetime.now(),
                            min_value=datetime(1900, 1, 1),
                            max_value=datetime(2200, 12, 31))

day_of_year = target_date.timetuple().tm_yday
n = 365 if day_of_year > 365 else day_of_year

indices = get_chronological_indices(n)
labels = ["Index -120", "Index -80", "Index -40", 
          f"Day {n} Tahun Ini", 
          "Index +40", "Index +80", "Index +120"]

st.write("---")

# --- 4. RENDER KRONOLOGIS (-120 ke +120) ---
for i, idx in enumerate(indices):
    if idx in DATA_YAWM:
        d = DATA_YAWM[idx]
        if i == 3:
            # Fokus Day X (Cukup Bolding tanpa simbol)
            st.markdown(f"**{labels[i]} | {idx}**")
            st.markdown(f"**{d[0]} {d[1]}:{d[2]}**")
            st.markdown(f"**{d[3]}**")
        else:
            # Index lainnya
            st.write(f"{labels[i]} | {idx}")
            st.write(f"{d[0]} {d[1]}:{d[2]}")
            st.write(d[3])
    else:
        st.write(f"{labels[i]} | {idx}")
        st.write("Data belum diinput")
    
    st.write("---")

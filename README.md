# What Message Today (1900-2200)

Sistem algoritma untuk memetakan waktu linear (Masehi) ke dalam siklus pesan "Yawm" (365 frekuensi).

## Spesifikasi
- **Epoch:** 1 Januari 1900
- **Range:** 1900 hingga 31 Desember 2200
- **Logic:** ((Total Days from Epoch) % 365), index 1-based (1-365)
- **Database:** 365 kata 'Yawm' (tunggal) dalam Al-Qur'an

## Struktur File
| File | Deskripsi |
|------|-----------|
| yawm_logic.py | Modul logika inti (kalkulasi index, tafsir) |
| main.py | CLI interface |
| streamlit_app.py | Web UI (Streamlit) |
| database_yawm.py | Database 365 entri Yawm |

## Cara Menjalankan

### CLI
    python main.py

### Web UI (Streamlit)
    pip install -r requirements.txt
    streamlit run streamlit_app.py

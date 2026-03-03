import datetime
from database_yawm import DATA_YAWM

def what_message_today():
    print("="*60)
    print(" " * 20 + "WHAT MESSAGE TODAY")
    print("="*60)
    
    try:
        tgl = int(input("Tanggal (DD): "))
        bln = int(input("Bulan (MM): "))
        thn = int(input("Tahun (YYYY): "))
        
        target_date = datetime.date(thn, bln, tgl)
        start_date = datetime.date(1990, 1, 1)
        
        if not (1990 <= thn <= 2200):
            print("(!) ERROR: Out of System Range (1990-2200)")
            return

        hari_ke = (target_date - start_date).days + 1
        indeks = hari_ke % 365
        if indeks == 0: indeks = 365
        
        print(f"\nSINKRONISASI: {target_date.strftime('%d %B %Y')}")
        print(f"HARI KE-    : {hari_ke}")
        print(f"INDEX YAWM  : {indeks}")
        print("-" * 60)

        # Mengambil data dari file database_yawm.py
        if indeks in DATA_YAWM:
            surah, no, ayat, pesan = DATA_YAWM[indeks]
            print(f"MESSAGE: {surah} ({no}):{ayat}\n\"{pesan}\"")
        else:
            print(f"MESSAGE: Index {indeks} is waiting for synchronization.")
        
        print("-" * 60)

    except ValueError:
        print("(!) INPUT ERROR")

if __name__ == "__main__":
    what_message_today()
  

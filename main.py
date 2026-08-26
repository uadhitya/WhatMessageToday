"""
main.py — CLI interface untuk sistem WhatMessageToday.
"""

import datetime
from yawm_logic import calculate_yawm_index, get_yawm_data, validate_year, YEAR_MIN, YEAR_MAX


def what_message_today():
    print("=" * 60)
    print(" " * 20 + "WHAT MESSAGE TODAY")
    print("=" * 60)

    try:
        tgl = int(input("Tanggal (DD): "))
        bln = int(input("Bulan (MM): "))
        thn = int(input("Tahun (YYYY): "))

        if not validate_year(thn):
            print(f"(!) ERROR: Out of System Range ({YEAR_MIN}-{YEAR_MAX})")
            return

        target_date = datetime.date(thn, bln, tgl)
        hari_ke, indeks = calculate_yawm_index(target_date)

        print(f"\nSINKRONISASI: {target_date.strftime('%d %B %Y')}")
        print(f"HARI KE-    : {hari_ke}")
        print(f"INDEX YAWM  : {indeks}")
        print("-" * 60)

        data = get_yawm_data(indeks)
        if data:
            surah, no, ayat, pesan = data
            print(f'MESSAGE: {surah} ({no}):{ayat}\n"{pesan}"')
        else:
            print(f"MESSAGE: Index {indeks} is waiting for synchronization.")

        print("-" * 60)

    except ValueError:
        print("(!) INPUT ERROR")


if __name__ == "__main__":
    what_message_today()

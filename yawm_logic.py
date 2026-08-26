import datetime
from database_yawm import DATA_YAWM

# Konstanta sistem
EPOCH = datetime.date(1900, 1, 1)
YEAR_MIN = 1900
YEAR_MAX = 2200
CYCLE_LENGTH = 365


def calculate_yawm_index(target_date):
    hari_ke = (target_date - EPOCH).days + 1
    indeks = hari_ke % CYCLE_LENGTH
    if indeks == 0:
        indeks = CYCLE_LENGTH
    return hari_ke, indeks


def get_yawm_data(indeks):
    return DATA_YAWM.get(indeks)


def get_tafsir_indices(n):
    sebab = [((n - d - 1) % CYCLE_LENGTH) + 1 for d in [120, 80, 40]]
    petunjuk = [((n + d - 1) % CYCLE_LENGTH) + 1 for d in [40, 80, 120]]
    return sebab, petunjuk


def validate_year(year):
    return YEAR_MIN <= year <= YEAR_MAX

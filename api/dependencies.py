import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'model' / 'model.h5'
CLASS_NAMES = [
    'Dadar Gulung',
    'Kastengel',
    'Klepon',
    'Roti Lapis',
    'Kue Lumpur',
    'Putri Salju',
    'Risoles',
    'Serabi'
]


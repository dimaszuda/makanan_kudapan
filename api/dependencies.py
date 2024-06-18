import os
from pathlib import Path

# Menentukan path relatif ke file model.h5
MODEL_PATH = Path(__file__).parent.parent / 'model' / 'model.h5'

# Mengubah ke path absolut jika diperlukan
MODEL_PATH = MODEL_PATH.resolve()

MODEL_DOCKER = os.getenv('MODEL_PATH', 'model/model.h5')

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


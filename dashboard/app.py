import os
import sys
import streamlit as st
import tensorflow as tf
from pathlib import Path
from utils import (
    load_model,
    show_image,
    detect_image
)
# config page and layout
st.set_page_config(
    page_title="Deteksi Makanan Kudapan",
    layout="wide",
    
)

# define class names
CLASSES_NAME = [
    'Dadar Gulung',
    'Kastengel',
    'Klepon',
    'Roti Lapis',
    'Kue Lumpur',
    'Putri Salju',
    'Risoles',
    'Serabi'
]

# image format that are allowed to be uploaded
IMG_TYPE = [
    'jpg',
    'png',
    'jpeg',
    'webp',
]

# Menentukan path relatif ke file model.h5
MODEL_PATH = Path(__file__).parent.parent / 'model' / 'model.h5'

# Mengubah ke path absolut jika diperlukan
MODEL = MODEL_PATH.resolve()

MODEL_DOCKER = os.getenv('MODEL_PATH', 'model/model.h5')

# Title of streamlit application
st.title("Deteksi Makanan Kudapan Indonesia")

sys.setrecursionlimit(1500)

class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(CustomLayer, self).__init__(**kwargs)
    
    def call(self, inputs):
        return inputs * 2
    
def load_my_model(model_path: Path):
    try:
        model = tf.keras.models.load_model(model_path, custom_objects={'CustomLayer': CustomLayer})
        st.success("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None
    
st.write("Load and Use a TensorFlow Model in Streamlit")
# Load the model
model = load_my_model(MODEL_DOCKER)

image = st.file_uploader("Upload an image", type=IMG_TYPE)

if image:
    show_image(image)
    name = detect_image(image, model, CLASSES_NAME=CLASSES_NAME)
    if name:
        st.success("Success Detect Image")
        st.write(f"The cake name of this image is: {name}")
    else:
        st.error("Cannot Detect Image")
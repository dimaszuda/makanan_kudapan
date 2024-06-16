import numpy as np
import streamlit as st
from pathlib import Path
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

def load_model(model_path: Path):
    """
    Load the Base Model
    Args:
        model_path (Path): path of the saved model
    return:
    Model: model
    """
    model = load_model(model_path)
    return model

def show_image(img_path: Path) -> None:
    """ Show the original image
    Args: 
        img_path (Path): path to uploaded image
    returns:
        None
    """
    try:
        st.image(
            img_path,
            caption="Original Image",
            use_column_width=True
        )
    except Exception as e:
        st.error(f"Error Load Image: {e}")

def detect_image(image_path: Path, model, CLASSES_NAME) -> str:
    """
    Detect the cake name from the image
    Args:
        image_path (Path): path to uploaded image
        model: model ML used
        CLASSES_NAME (List): List of class names
    returns:
    str: name of class
    """
    img = load_img(image_path, target_size=(150, 150))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img = np.vstack([x])
    classes = model.predict(img, batch_size=10)
    class_name = CLASSES_NAME[np.argmax(classes)]
    return class_name    
import numpy as np
import tensorflow as tf
from pathlib import Path
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array


static_folder = Path("static").resolve()
def upload_file(document) -> str:
    if document is None:
        return None
    try:
        if document.filename.lower().endswith(("jpg", "png", "jpeg", "webp")):
            img_path = static_folder / document.filename
            with open(img_path, mode="wb") as file_obj:
                content = document.file.read()
                file_obj.write(content)
            # add dict to save img attributes such as filename, height, width
            return img_path
    except Exception as e:
        return None
    
class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(CustomLayer, self).__init__(**kwargs)
    
    def call(self, inputs):
        return inputs * 2
    
def loadModel(model_path: Path):
    model = load_model(model_path, custom_objects={'CustomLayer': CustomLayer})
    return model
    
def detect_img(img_path: Path, model, class_names: list) -> str:
    try:
        img = load_img(img_path, target_size=(150, 150))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img = np.vstack([x])
        classes = model.predict(img, batch_size=10)
        class_name = class_names[np.argmax(classes)]
        return class_name 
    except Exception as e:
        return None
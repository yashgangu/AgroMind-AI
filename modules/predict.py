import tensorflow as tf
import numpy as np
from PIL import Image
import os

# LOAD MODEL

model = tf.keras.models.load_model(
    "crop_disease_model.h5",
    compile=False
)

# DATASET PATH

dataset_path = "dataset"

# CLASS NAMES

class_names = sorted([
    folder for folder in os.listdir(dataset_path)
    if os.path.isdir(os.path.join(dataset_path, folder))
])

# PREDICTION FUNCTION

def predict_disease(image):

    image = image.convert("RGB")

    image = image.resize((224, 224))

    img_array = np.array(image)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_index = np.argmax(prediction)

    predicted_class = class_names[predicted_index]

    confidence = float(np.max(prediction))

    # SPLIT CROP & DISEASE

    parts = predicted_class.split("___")

    crop = parts[0]

    disease = parts[1] if len(parts) > 1 else "Healthy"

    # CLEAN TEXT

    crop = crop.replace("_", " ")

    disease = disease.replace("_", " ")

    return crop, disease, confidence
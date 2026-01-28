import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input

# ---------------- CONFIG ----------------
MODEL_PATH = "../models/resnet_finetuned_best.h5"
IMAGE_DIR = "../external_test_images"
IMG_SIZE = (224, 224)

# ---------------- LOAD MODEL ----------------
model = tf.keras.models.load_model(MODEL_PATH)

class_names = [
    'potato_bacteria',
    'potato_fungi',
    'potato_healthy',
    'potato_nematode',
    'potato_phytopthora',
    'potato_virus',
    'rice_bacterial_leaf_blight',
    'rice_brown_spot',
    'rice_healthy',
    'rice_leaf_blast',
    'rice_leaf_scald',
    'rice_sheath_blight'
]

# ---------------- PREDICT EXTERNAL IMAGES ----------------
for img_name in os.listdir(IMAGE_DIR):
    img_path = os.path.join(IMAGE_DIR, img_name)

    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    pred_class = class_names[np.argmax(preds)]
    confidence = np.max(preds) * 100

    # -------- DISPLAY --------
    plt.figure(figsize=(4, 4))
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"{pred_class}\nConfidence: {confidence:.1f}%")
    plt.show()

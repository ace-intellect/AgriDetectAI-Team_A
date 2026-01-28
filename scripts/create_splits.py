import os
import shutil
from sklearn.model_selection import train_test_split

RAW_DIR = "../raw_data"
OUT_DIR = "../processed_data"

TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

os.makedirs(OUT_DIR, exist_ok=True)

def copy_images(image_list, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)
    for img in image_list:
        shutil.copy(img, dest_folder)

for crop in os.listdir(RAW_DIR):
    crop_path = os.path.join(RAW_DIR, crop)

    for cls in os.listdir(crop_path):
        class_path = os.path.join(crop_path, cls)
        images = [os.path.join(class_path, img) for img in os.listdir(class_path)]

        train_imgs, temp_imgs = train_test_split(images, test_size=0.3, random_state=42)
        val_imgs, test_imgs = train_test_split(temp_imgs, test_size=0.5, random_state=42)

        copy_images(train_imgs, os.path.join(OUT_DIR, "train", cls))
        copy_images(val_imgs, os.path.join(OUT_DIR, "val", cls))
        copy_images(test_imgs, os.path.join(OUT_DIR, "test", cls))

print("Dataset split completed successfully.")

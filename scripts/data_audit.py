import os
from PIL import Image
from tqdm import tqdm

RAW_DATA_DIR = "../raw_data"

def is_image_valid(img_path):
    try:
        with Image.open(img_path) as img:
            img.verify()
        return True
    except:
        return False

bad_images = []

for crop in os.listdir(RAW_DATA_DIR):
    crop_path = os.path.join(RAW_DATA_DIR, crop)
    if not os.path.isdir(crop_path):
        continue

    for class_name in os.listdir(crop_path):
        class_path = os.path.join(crop_path, class_name)

        for img_name in tqdm(os.listdir(class_path), desc=f"Checking {class_name}"):
            img_path = os.path.join(class_path, img_name)

            if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
                bad_images.append(img_path)
                continue

            if not is_image_valid(img_path):
                bad_images.append(img_path)

print(f"\nTotal corrupted/invalid images: {len(bad_images)}")

with open("bad_images.txt", "w") as f:
    for img in bad_images:
        f.write(img + "\n")

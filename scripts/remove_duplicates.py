import os
import cv2
from imutils import paths
from tqdm import tqdm

RAW_DATA_DIR = "../raw_data"
hashes = {}
duplicates = []

def dhash(image, hashSize=8):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

image_paths = list(paths.list_images(RAW_DATA_DIR))

for imagePath in tqdm(image_paths, desc="Scanning duplicates"):
    image = cv2.imread(imagePath)
    if image is None:
        continue

    h = dhash(image)

    if h in hashes:
        duplicates.append(imagePath)
    else:
        hashes[h] = imagePath

print(f"Found {len(duplicates)} duplicate images")

for dup in duplicates:
    os.remove(dup)

print("Duplicates removed.")

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

from sklearn.metrics import classification_report, confusion_matrix

from data_generators import test_gen

# ---------------- LOAD MODEL ----------------
model = tf.keras.models.load_model("../models/resnet_finetuned_best.h5")

# ---------------- PREDICTIONS ----------------
test_gen.reset()
pred_probs = model.predict(test_gen, verbose=1)
y_pred = np.argmax(pred_probs, axis=1)
y_true = test_gen.classes

class_names = list(test_gen.class_indices.keys())

# ---------------- CLASSIFICATION REPORT ----------------
print("\n=== Classification Report ===\n")
print(classification_report(y_true, y_pred, target_names=class_names))

# ---------------- CONFUSION MATRIX ----------------
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(14, 12))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()

# ---------------- SAMPLE PREDICTIONS (MIXED CLASSES) ----------------
num_samples = 12
indices = random.sample(range(len(y_true)), num_samples)

plt.figure(figsize=(18, 10))

for i, idx in enumerate(indices):
    img_path = test_gen.filepaths[idx]
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)

    plt.subplot(3, 4, i + 1)
    plt.imshow(img_array.astype("uint8"))
    plt.axis("off")

    true_label = class_names[y_true[idx]]
    pred_label = class_names[y_pred[idx]]
    confidence = np.max(pred_probs[idx]) * 100

    color = "green" if true_label == pred_label else "red"
    plt.title(
        f"True: {true_label}\nPred: {pred_label}\nConf: {confidence:.1f}%",
        color=color,
        fontsize=9
    )

plt.suptitle("Sample Test Predictions (Mixed Classes)", fontsize=16)
plt.tight_layout()
plt.show()

# ---------------- PER-CLASS ACCURACY ----------------
class_accuracy = {}

for i, class_name in enumerate(class_names):
    idxs = np.where(y_true == i)[0]
    class_acc = np.mean(y_pred[idxs] == y_true[idxs])
    class_accuracy[class_name] = class_acc

plt.figure(figsize=(12, 6))
plt.bar(class_accuracy.keys(), class_accuracy.values())
plt.xticks(rotation=45, ha="right")
plt.ylabel("Accuracy")
plt.title("Per-Class Accuracy")
plt.tight_layout()
plt.show()

# ---------------- CONFIDENCE DISTRIBUTION ----------------
confidences = np.max(pred_probs, axis=1)

plt.figure(figsize=(8, 5))
plt.hist(confidences, bins=20)
plt.xlabel("Prediction Confidence")
plt.ylabel("Number of Samples")
plt.title("Model Confidence Distribution on Test Set")
plt.tight_layout()
plt.show()

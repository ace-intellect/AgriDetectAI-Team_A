 

---

# AgriDetectAI: Rice & Potato Disease Classification

**AgriDetectAI** is a deep learning project designed to classify diseases in rice and potato leaves. It utilizes a unified model approach, allowing users to upload leaf images without manually specifying the crop type, thereby improving usability and scalability.

## 📌 Project Overview

The core architecture of this project is based on **ResNet50**, a deep residual network pretrained on the ImageNet dataset. This model was chosen for its ability to mitigate the vanishing gradient problem and its effectiveness in learning fine-grained visual patterns such as leaf discoloration and lesions.

* 
**Primary Goal:** Accurate disease classification for rice and potato plants.


* 
**Total Classes:** 12 (including healthy and diseased conditions).


* 
**Model Accuracy:** 98%.



## 📂 Dataset

The dataset consists of images covering both healthy and diseased conditions for rice and potatoes. The data was cleaned to remove corrupted or duplicate images before training.

### Classes

The model classifies images into the following **12 categories**:

| **Crop** | **Disease/Condition** |
| --- | --- |
| **Potato** | Bacteria, Fungi, Healthy, Nematode, Phytopthora, Virus |
| **Rice** | Bacterial Leaf Blight, Brown Spot, Healthy, Leaf Blast, Leaf Scald, Sheath Blight |

### Data Split Strategy

To avoid data leakage and ensure reliable evaluation, the dataset was split as follows:

* 
**Training Set:** 70% 


* 
**Validation Set:** 15% 


* 
**Test Set:** 15% (Truly unseen data) 



## 🏗️ Model Architecture

The model uses a Transfer Learning approach with the following structure:

* 
**Backbone:** ResNet50 (Pretrained on ImageNet, top layers removed).


* **Custom Classification Head:**
* Global Average Pooling.


* Dense Layer with ReLU activation.


* Dropout Layer (to reduce overfitting).


* Final Softmax Layer (for 12-class classification).





## ⚙️ Training Strategy

The training process was divided into two distinct phases to maximize performance.

### Phase 1: Feature Extraction

* 
**Method:** All layers of the ResNet50 backbone were **frozen**.


* 
**Goal:** Train only the custom classification head to learn task-specific patterns while preserving pretrained features.



### Phase 2: Fine-Tuning

* 
**Method:** Top layers of ResNet50 were **unfrozen**.


* 
**Goal:** Adapt high-level features specifically to rice and potato disease patterns using a lower learning rate.



### Callbacks Used

* 
**Early Stopping:** To prevent overfitting.


* 
**ReduceLROnPlateau:** For stable convergence.


* 
**Model Checkpointing:** To save the best-performing model.



## 📊 Performance & Results

The model was evaluated using Accuracy, Precision, Recall, F1-score, and a Confusion Matrix.

### Key Metrics

* 
**Overall Accuracy:** **98%**.


* 
**Macro Average F1-Score:** 0.98.


* 
**Performance:** High precision and recall were achieved across most classes, with minor performance drops only observed in visually similar diseases.



### Visual Analysis

* 
**Accuracy & Loss Curves:** Training and validation accuracy increased steadily, while loss decreased consistently, indicating effective optimization with minimal overfitting.


* 
**Confusion Matrix:** Shows strong diagonal dominance, confirming correct predictions for the majority of samples.



## 🧪 Qualitative Testing

In addition to quantitative metrics, the model was tested on unseen images, including external images collected from online sources.

* 
**Results:** The model demonstrated logical disease identification with high confidence scores for correct predictions.


* 
**Generalization:** Validated effectiveness on real-world images.



## 📝 Conclusion

A single unified ResNet50-based model was successfully trained, demonstrating high accuracy and strong generalization across all 12 disease classes.

---


# 🐾 Animal Image Classification Using EfficientNetB3

This project uses a deep learning model (EfficientNetB3) to classify images of animals into 90 species. A user-friendly web interface built with **Streamlit** allows users to upload animal images and instantly receive classification results with confidence scores.

![Project Banner](images/banner.jpg) <!-- Replace with actual image -->

## 📌 Table of Contents

1. [Introduction](#-introduction)
2. [Abstract](#-abstract)
3. [Purpose](#-purpose)
4. [Literature Survey](#-literature-survey)
5. [Region of Interest](#-region-of-interest)
6. [Proposed System](#-proposed-system)
7. [Block Diagram](#-block-diagram)
8. [Algorithm](#-algorithm)
9. [Implementation](#-implementation)
10. [System Architecture](#-system-architecture)
11. [Output / Results](#-output--results)
12. [Conclusion](#-conclusion)
13. [Future Scope](#-future-scope)

---

## 💡 Introduction

Animal Image Classification is a computer vision task using **EfficientNet**, a deep learning model that identifies animals based on features like shape, color, texture, etc.

---

## 📜 Abstract

A Streamlit-based web app uses EfficientNetB3 to classify 90 animal species with high accuracy. It provides fast and reliable results, aiding in fields like wildlife monitoring and conservation.

---

## 🎯 Purpose

- Automate animal identification
- Reduce manual image labeling
- Aid in wildlife monitoring and biodiversity tracking
- Provide a scalable and efficient classification tool

---

## 📚 Literature Survey

| Model     | Summary |
|-----------|---------|
| VGGNet    | Deep but slow |
| ResNet    | Skip connections, improved accuracy |
| MobileNet | Lightweight, limited accuracy |
| **EfficientNet** | Best trade-off of size and accuracy |

---

## 🔍 Region of Interest (ROI)

- Focuses on the part of the image where the animal is present
- Removes background noise
- Improves model accuracy
- Often extracted using **YOLO** or **Faster R-CNN**

![ROI Example](images/roi_example.jpg) <!-- Replace with actual image -->

---

## 🚀 Proposed System

The system is built using **EfficientNetB3**, pre-trained on ImageNet and fine-tuned on our dataset.

### Steps:

1. **Image Input** – via Streamlit
2. **Preprocessing** – Resize to 224x224 and normalize
3. **Feature Extraction** – Via EfficientNetB3
4. **Result Display** – Animal name and confidence score shown

---

## 📊 Block Diagram

![Block Diagram](images/block_diagram.jpg) <!-- Replace with actual image -->

---

## 🧠 Algorithm

EfficientNetB3 uses compound scaling to balance depth, width, and resolution, leading to higher accuracy and efficiency. Transfer learning is applied for adaptation to animal species.

---

## 🛠️ Implementation

1. **Dataset** – 90 species, includes animals like cats, dogs, lions, elephants.
2. **Preprocessing** – Resize, normalize, split into train/test.
3. **Model Training** – Fine-tuned EfficientNetB3 using TensorFlow/Keras.
4. **Classification** – Predict species from uploaded image.

---

## 🖥️ System Architecture

### Hardware
- CPU: Intel i5/Ryzen 5+
- GPU: GTX 1060/RTX 2060 (4GB+)
- RAM: 8GB+ (16GB recommended)
- SSD: 20GB+ free space

### Software
- Python 3.7+
- TensorFlow 2.x, PyTorch
- Libraries: Pillow, NumPy, Matplotlib

---

## ✅ Advantages

- Fast and accurate classification
- Useful for conservation and biodiversity research
- Automates manual image analysis
- Supports edge devices and web deployment

---

## 🖼️ User Interface

![UI Screenshot](images/ui_screenshot.jpg) <!-- Replace with actual image -->

---

## 📈 Output / Results

![Output Example](images/output_result.jpg) <!-- Replace with actual image -->

---

## 🔮 Future Scope

- Wildlife conservation and poaching detection
- Livestock monitoring and breed identification
- Smart pet devices and vet diagnostics
- Educational mobile apps
- Multimodal tracking with sound and video

---

## 🧾 Conclusion

EfficientNetB3 provides an effective, accurate, and scalable solution for animal classification. This system can support education, conservation, and various real-world applications by automating image-based animal recognition.

---

## 🙏 Acknowledgements

Guided by **Ms. Gowthami, M.Tech**, Assistant Professor  
**Kakinada Institute of Engineering and Technology - II**

---

## 👨‍💻 Developed By

- K. Pavan Kumar – 216Q1A4220  
- T. Ravali – 216Q1A4202  
- K. Naga Sidhartha Rohith – 216Q1A4249  
- K. Shanmuka Naga Sai – 216Q1A4254  
- G. Ajay Kumar – 216Q1A4232  

---

### 📂 Image Setup Instructions

To ensure all images appear in the README:

1. Extract the necessary images from the PPT as `.jpg` or `.png`.
2. Create a folder named `images/` in the root of your repo.
3. Save all extracted images with the filenames used in the placeholders (e.g., `roi_example.jpg`, `block_diagram.jpg`, etc.)
4. Commit and push the `images/` folder along with the README.

---

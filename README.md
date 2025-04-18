# Live Sign Language Detection and Body Segmentation using YOLOv8

## 🚀 Preview
Here are some snapshots of the the Website:

### Homepage
![Image](https://github.com/user-attachments/assets/c4f59e19-8d71-40a0-b763-b5c0bf92679d)

### Output
![Image](https://github.com/user-attachments/assets/5a4502d3-c6b8-46d7-bde7-7d76182b3c8c) ![Image](https://github.com/user-attachments/assets/dd5465ea-81a4-4cdd-b304-08113d539ea7)

This project is a real-time web application that uses YOLOv8 for two powerful computer vision tasks: **Sign Language Gesture Detection** and **Human Body Segmentation**. Built using Python and Flask, the system captures live webcam footage and applies trained deep learning models for interactive detection and segmentation.

## 🔍 Features

- **Real-Time Sign Detection**  
  Detects and classifies sign language gestures from a live webcam feed using a custom-trained YOLOv8 model.

- **Live Body Segmentation**  
  Uses YOLOv8 segmentation capabilities to outline and segment the full human body in real time.

- **Web-Based Interface**  
  Simple, interactive Flask frontend to view results and switch between modes (`sign` or `segmentation`).

- **Toggle Modes**  
  Easily switch between sign detection and segmentation by changing the route or query parameter.

## 🧠 Technologies Used

- **Python**
- **Flask**
- **OpenCV**
- **YOLOv8 (Ultralytics)**
- **HTML/CSS**
- **Google Colab**

## 📁 File Structure
```
/ (Root Directory)
├── app.py                      # Main Flask application
├── templates/                  # HTML templates for frontend
│   ├── index.html              # Landing page
│   └── live_feed.html          # Live video stream display
├── sign_detection/            # Directory for sign detection models
│   ├── best.pt                 # Trained YOLOv8 model for sign gesture detection
│   └── yolov8s.pt              # Base YOLOv8s model used for transfer learning
├── segmentation_model/        # Directory for segmentation model
│   └── yolov8n-seg.pt          # YOLOv8 model for full-body segmentation
├── static/                    # Static files (CSS, JavaScript, images, etc.)
├── requirements.txt            # Python dependencies
```

## 🚀 Installation and Setup

1. **Clone the Repository**

```bash
git clone https://github.com/sumukhpshetty25/yolov8-sign-detection-segmentation.git
cd yolov8-sign-detection-segmentation
```
2. **Install Dependencies**
Make sure you have Python installed. Then run:
```bash
pip install -r requirements.txt
```
1. **Place Trained Models**
Ensure the following YOLOv8 models are placed in the correct directories:

Sign Detection Model:

sign_detection/best.pt
→ Trained model downloaded from Google Colab after training (train.ipynb)

sign_detection/yolov8s.pt
→ Pretrained YOLOv8s model downloaded from Ultralytics

Segmentation Model:

segmentation_model/yolov8n-seg.pt
→ YOLOv8n-seg model for body segmentation (also from Ultralytics)

## 📌 Notes
Make sure your webcam is connected and accessible by OpenCV.

You can train your own YOLOv8 models using Roboflow or Google Colab and update the .pt files.

For better real-time performance, use a machine with a GPU.

## 🛠️ Troubleshooting
Camera not found: Ensure no other apps are using your webcam.

Blank feed: Double-check model paths and make sure models are correctly placed.

Performance lag: Consider reducing frame resolution or using a smaller model variant.

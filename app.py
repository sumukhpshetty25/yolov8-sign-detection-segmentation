from flask import Flask, render_template, Response, request
from ultralytics import YOLO
import cv2

app = Flask(__name__)

# Paths to YOLO models
SIGN_MODEL_PATH = "C:/Users/Sumukh P Shetty/Desktop/Sign/Mini_Project/sign_detection/best.pt"
SEGMENTATION_MODEL_PATH = "C:/Users/Sumukh P Shetty/Desktop/Sign/Mini_Project/segmentation_model/yolov8n-seg.pt"

# Load models
sign_model = YOLO("C:/Users/Sumukh P Shetty/Desktop/Sign/Mini_Project/sign_detection/best.pt")
segmentation_model = YOLO("C:/Users/Sumukh P Shetty/Desktop/Sign/Mini_Project/segmentation_model/yolov8n-seg.pt")

# Global variables
cap = None

def generate_frames(model, conf=0.5):
    global cap
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Error: Unable to access the camera.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Predict with YOLO
        results = model.predict(source=frame, save=False, conf=conf, verbose=False)

        # Annotate the frame
        annotated_frame = results[0].plot() if results and len(results) > 0 else frame

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    mode = request.args.get('mode', 'sign')
    model = sign_model if mode == 'sign' else segmentation_model
    return Response(generate_frames(model), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/live_feed/<mode>')
def live_feed(mode):
    return render_template('live_feed.html', mode=mode)

if __name__ == "__main__":
    app.run(debug=True)

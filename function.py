import os
from ultralytics import YOLO
import cv2
import math

def train(path,epochs):
    # Load a model
    model = YOLO(path)
    # # Use the model
    results = model.train(data="data.yaml", epochs=epochs)

def predict_video(video,model):
    model = YOLO(model)
    cap = cv2.VideoCapture(video)

    classNames = ['Ball', 'Team1', 'Team2']
    while True:
        # Loading video
        success, img = cap.read()
        # Detection objects
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Getting x and y coordination of objects
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                # Getting confident and name of detected objects.
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                # Showing detected object and information about they
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 100, 200), 5)
                cv2.putText(img, f'{classNames[cls]}{conf}', (max(0, x1), max(40, y1 - 30)), 5, 1, (255, 100, 200))
        cv2.imshow("Image", img)
        cv2.waitKey(1)
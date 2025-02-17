import cv2
import numpy as np
from ultralytics import YOLO

class Detection:
    _instance = None
    def __init__(self, modelPath: str = "shared/data/yolov8n.pt"):
        if Detection._instance is None:
            Detection._instance = YOLO(modelPath)
        self.model = Detection._instance

    def detect(self, image: np.ndarray, uuid: str):
        if image is None:
            raise ValueError(f"Image not found: {image}")

        results = self.model(image)
        personCount = 0

        for result in results:
            for box in  result.boxes:
                classID = int(box.cls[0])
                if classID == 0:
                    personCount += 1

                    xyxy = box.xyxy[0].cpu().numpy().astype(int)
                    x1, y1, x2, y2 = xyxy

                    confidence = box.conf[0].cpu().numpy().astype(float)

                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    label = f"Person: {confidence:.2f}"
                    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        
        cv2.imwrite(f"{uuid}.jpg", image)
        return personCount, image

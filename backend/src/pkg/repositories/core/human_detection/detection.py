import os
import cv2
import numpy as np
from ultralytics import YOLO

from shared.config.detection import DetectionConf


class Detection:
    _instance = None

    def __init__(
        self, modelPath: str = "shared/data/yolov8n.pt", threshold: float = 0.5
    ):
        if Detection._instance is None:
            Detection._instance = YOLO(modelPath)
        self.model = Detection._instance
        self._warmup()

        if os.path.exists(f"{DetectionConf.savedImageDir}/input") is False:
            os.makedirs(f"{DetectionConf.savedImageDir}/input")
        if os.path.exists(f"{DetectionConf.savedImageDir}/output") is False:
            os.makedirs(f"{DetectionConf.savedImageDir}/output")
        self.threshold = threshold

    def _warmup(self):
        for i in range(5):
            dummy = np.zeros((640, 640, 3), dtype=np.uint8)
            _ = self.model(dummy)

    def loadImage(self, uuid):
        return cv2.imread(f"{DetectionConf.savedImageDir}/input/{uuid}.jpg")

    def detect(self, uuid: str):
        image = self.loadImage(uuid)
        results = self.model(image)
        personCount = 0

        for result in results:
            for box in result.boxes:
                classID = int(box.cls[0])
                if classID == 0:
                    xyxy = box.xyxy[0].cpu().numpy().astype(int)
                    x1, y1, x2, y2 = xyxy

                    confidence = box.conf[0].cpu().numpy().astype(float)
                    if confidence < self.threshold:
                        continue

                    personCount += 1
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    label = f"Person: {confidence:.2f}"
                    cv2.putText(
                        image,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (36, 255, 12),
                        2,
                    )

        cv2.imwrite(f"{DetectionConf.savedImageDir}/output/{uuid}.jpg", image)
        ret, buffer = cv2.imencode(".jpg", image)
        if not ret:
            raise Exception("Failed to encode image to JPEG")
        return personCount, buffer.tobytes()

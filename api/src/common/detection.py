import os
import cv2
import numpy as np
from ultralytics import YOLO


class Detection:
    _instance = None

    def __init__(
        self,
        modelPath: str = "shared/data/yolov8n.pt",
        imageSaveDir: str = None,
        threshold: float = 0.5,
    ):
        if Detection._instance is None:
            Detection._instance = YOLO(modelPath, verbose=False)
        self.model = Detection._instance
        self._warmup()

        self.imageSaveDir = imageSaveDir

        if os.path.exists(f"{imageSaveDir}/input") is False:
            os.makedirs(f"{imageSaveDir}/input")
        if os.path.exists(f"{imageSaveDir}/output") is False:
            os.makedirs(f"{imageSaveDir}/output")
        self.threshold = threshold

    def _warmup(self):
        for i in range(5):
            dummy = np.zeros((640, 640, 3), dtype=np.uint8)
            _ = self.model(dummy)

    def loadImage(self, uuid) -> cv2.typing.MatLike:
        return cv2.imread(f"{self.imageSaveDir}/input/{uuid}.jpg")

    def detect(self, uuid: str) -> tuple[int, bytes]:
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

        cv2.imwrite(f"{self.imageSaveDir}/output/{uuid}.jpg", image)
        ret, buffer = cv2.imencode(".jpg", image)
        if not ret:
            raise Exception("Failed to encode image to JPEG")
        return personCount, buffer.tobytes()

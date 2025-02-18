import uuid
import base64
import os
import shutil
from fastapi.responses import JSONResponse
from pkg.repositories.core.human_detection.detection import Detection
from pkg.repositories.postgre.core_manager import CoreManager

from shared.config.detection import DetectionConf
from shared.config.postgre import PostgreConf


class CompressImage:
    @staticmethod
    def compress(image):
        return base64.b64encode(image)


class CoreUseCases:
    def __init__(self):
        self.detection = Detection(modelPath=DetectionConf.modelDir)
        self.coreManager = CoreManager(
            host=PostgreConf.host,
            port=PostgreConf.port,
            user=PostgreConf.user,
            password=PostgreConf.pwd,
            dbname=PostgreConf.db,
        )
        self.coreManager.createTable()
        self.compressImage = CompressImage()

    async def detect(self, uuid):
        return self.detection.detect(uuid)
    
    def insert(self, uuid, personCount):
        self.coreManager.insert(uuid, personCount)

    def saveInputImage(self, uuid, image):
        with open(f"{DetectionConf.savedImageDir}/input/{uuid}.jpg", "wb") as f:
            shutil.copyfileobj(image.file, f)

    async def __call__(self, image):
        saveID = uuid.uuid4()
        self.saveInputImage(saveID, image)
        personCount, image = await self.detect(saveID)
        self.coreManager.insert(saveID, personCount)
        image = self.compressImage.compress(image)
        return JSONResponse(
            content={
                "code": 200,
                "message": "Success",
                "data": {"personCount": personCount, "image": image.decode("utf-8")},
            }
        )

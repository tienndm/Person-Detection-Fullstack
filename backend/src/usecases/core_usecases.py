import uuid
import base64
from pkg.repositories.core.human_detection.detection import Detection
from pkg.repositories.postgre.core_manager import CoreManager

from shared.config.postgre import PostgreConf
from shared.config.detection import DetectionConf

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
            database=PostgreConf.db,
        )
        self.coreManager.createTable()
        self.compressImage = CompressImage()

    def detect(self, image):
        uuid = uuid.uuid4()
        return self.detection.detect(image)

    def __call__(self, image):
        personCount, image = self.detect(image)
        self.coreManager.insert(uuid, personCount)
        image = self.compressImage.compress(image)
        return personCount, image


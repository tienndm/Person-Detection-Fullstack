from .base import DetectionConf
from common.detection import Detection

DetectionEngine = Detection(
    modelPath=DetectionConf.modelDir,
    imageSaveDir=DetectionConf.savedImageDir,
    threshold=DetectionConf.threshold,
)

saveImageDir = DetectionConf.savedImageDir

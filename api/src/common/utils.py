import shutil
import base64

from uuid import uuid4

from settings.person_detect import saveImageDir


def build_uui4_str() -> str:
    return str(uuid4().hex)


def public_dict(object_):
    return {k: v for k, v in vars(object_).items() if not k.startswith('_')}


def compress(image) -> bytes:
    return base64.b64encode(image)

def saveImage(uuid: str, image):
    with open(f'{saveImageDir}/input/{uuid}.jpg', "wb") as f:
        shutil.copyfileobj(image.file, f)
from common.docstring import MAPPER_DOCSTRING
from models.person_detect import RecordModel
from .schema import RecordResponse

class RecordResponseMapper:
    @staticmethod
    def entityToResponse(instance: RecordModel) -> RecordResponse:
        return RecordResponse(
            id=instance.id,
            personCount=instance.personCount,
            outputSaveDir=f'output/{instance.imageUUID}.jpg',
            createdAt=instance.createdAt
        )
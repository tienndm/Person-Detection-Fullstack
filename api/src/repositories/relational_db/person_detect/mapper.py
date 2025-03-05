from common.docstring import MAPPER_DOCSTRING
from models.person_detect import RecordModel

from .orm import PersonDetect


__doc__ = MAPPER_DOCSTRING


class PersonDetectOrmMapper:
    @staticmethod
    def ormToEntity(personDetect: PersonDetect) -> RecordModel:
        return RecordModel(
            id=personDetect.id,
            personCount=personDetect.person_count,
            imageUUID=personDetect.image_uuid,
            createdAt=personDetect.createdAt
        )

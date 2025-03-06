from common.docstring import MAPPER_DOCSTRING
from models.person_detect import RecordModel

from .orm import PersonDetect
from datetime import timedelta


__doc__ = MAPPER_DOCSTRING


class PersonDetectOrmMapper:
    @staticmethod
    def ormToEntity(personDetect: PersonDetect) -> RecordModel:
        gmt7CreatedAt = personDetect.createdAt + timedelta(hours=7) if personDetect.createdAt else None
        return RecordModel(
            id=personDetect.id,
            personCount=personDetect.person_count,
            imageUUID=personDetect.image_uuid,
            createdAt=gmt7CreatedAt,
        )

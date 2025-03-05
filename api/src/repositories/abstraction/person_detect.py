import abc
from typing import Any, List, Optional

from models.person_detect import RecordModel, GetRecordModel


class AbstractPersonRepository(abc.ABC):
    session: any

    @abc.abstractmethod
    async def list(self, params: Optional[GetRecordModel] = None) -> List[RecordModel]:
        raise NotImplementedError

    @abc.abstractmethod
    async def create(self, data: RecordModel) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, id: int):
        raise NotImplementedError

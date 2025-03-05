from typing import Callable, List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import delete, func, insert, select, update

from common.type import UUIDStr
from models.person_detect import RecordModel, GetRecordModel

from ...abstraction import AbstractPersonRepository
from .mapper import PersonDetectOrmMapper
from .orm import PersonDetect

func: Callable


class RelationalDBPersonDetectRepository(AbstractPersonRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self, params: Optional[GetRecordModel] = None) -> List[RecordModel]:
        stmt = select(PersonDetect)
        if params:
            stmt = stmt.offset((params.page - 1) * params.size).limit(params.size)
        record = (await self.session.execute(stmt)).scalars().all()
        return list(map(PersonDetectOrmMapper.ormToEntity, record))

    async def create(self, data: RecordModel) -> str:
        stmt = insert(PersonDetect).values(
            person_count=data.personCount, image_uuid=data.imageUUID
        )
        await self.session.execute(stmt)

        return data.imageUUID

    async def delete(self, id):
        stmt = delete(PersonDetect).where(PersonDetect.id == id)
        result = await self.session.execute(stmt)
        if result.rowcount == 0:
            raise 

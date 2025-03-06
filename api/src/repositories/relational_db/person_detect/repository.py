from typing import Callable, List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import delete, func, insert, select, update

from common.type import UUIDStr
from models.person_detect import RecordModel, GetRecordParamsModel, TotalPageModel

from ...abstraction import AbstractPersonRepository
from .mapper import PersonDetectOrmMapper
from .orm import PersonDetect

func: Callable


class RelationalDBPersonDetectRepository(AbstractPersonRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(
        self, params: Optional[GetRecordParamsModel] = None
    ) -> List[RecordModel]:
        stmt = select(PersonDetect).order_by(PersonDetect.id.desc())
        if params:
            stmt = stmt.offset((params.page - 1) * params.size).limit(params.size)
        record = (await self.session.execute(stmt)).scalars().all()

        result = []
        for i, item in enumerate(record):
            entity = PersonDetectOrmMapper.ormToEntity(item)
            entity.id = (params.page - 1) * params.size + i + 1 if params else i + 1
            result.append(entity)
        return result

    async def create(self, data: RecordModel) -> str:
        stmt = insert(PersonDetect).values(
            person_count=data.personCount, image_uuid=data.imageUUID
        )
        await self.session.execute(stmt)

        return data.imageUUID
    
    async def get(self, params: Optional[GetRecordParamsModel] = None) -> int:
        stmt = select(func.count()).select_from(PersonDetect)
        totalRecords = (await self.session.execute(stmt)).scalar_one()
        
        if not params or params.size <= 0:
            return 1
        
        totalPages = (totalRecords + params.size - 1) // params.size
        
        return max(1, totalPages)


    async def delete(self, id):
        stmt = delete(PersonDetect).where(PersonDetect.id == id)
        result = await self.session.execute(stmt)
        if result.rowcount == 0:
            raise

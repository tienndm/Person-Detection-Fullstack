from fastapi import File
from typing import Any, Tuple
from common.utils import build_uui4_str, compress, saveImage

from di.unit_of_work import AbstractUnitOfWork, AbstractDetectionUnitOfWork
from models.person_detect import RecordModel, GetRecordParamsModel, TotalPageModel


async def detectPerson(
    asyncUnitOfWork: AbstractUnitOfWork, unitOfWork: AbstractDetectionUnitOfWork, image: File 
) -> Tuple[RecordModel, bytes]:
    id = build_uui4_str()
    saveImage(id, image)
    personCount, image = await unitOfWork.detectPersons(id)
    image = compress(image)
    record = RecordModel(personCount=personCount, imageUUID=id)
    async with asyncUnitOfWork as auow:
        await auow.personDetectionRepo.create(record)

    return record, image


async def getRecord(asyncUnitOfWork: AbstractUnitOfWork, page: int) -> list[RecordModel]:
    getRecordParams = GetRecordParamsModel(page=page, size=10)
    async with asyncUnitOfWork as auow:
        return await auow.personDetectionRepo.list(getRecordParams)

async def getTotalPage(asyncUnitOfWork: AbstractUnitOfWork) -> TotalPageModel:
    getRecordParams = GetRecordParamsModel()
    async with asyncUnitOfWork as auow:
        return await auow.personDetectionRepo.get(getRecordParams)
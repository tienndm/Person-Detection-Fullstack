from fastapi import UploadFile, File
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from di.dependency_injection import injector
from di.unit_of_work import AbstractUnitOfWork, AbstractDetectionUnitOfWork
from usecases import person_detect as detectUsecase

from .schema import RecordResponse
from .mapper import RecordResponseMapper

router = APIRouter()


@router.post("/api/v1/core")
async def core(img: UploadFile = File(...)):
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    unitOfWork = injector.get(AbstractDetectionUnitOfWork)
    record, image = await detectUsecase.detectPerson(asyncUnitOfWork, unitOfWork, img)

    return JSONResponse(
        content={
            "code": 200,
            "message": "success",
            "data": {"personCount": record.personCount, "image": image.decode("utf-8")},
        }
    )


@router.get("/api/v1/fetch/{page}")
async def record(page: int) -> list[RecordResponse]:
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    records = await detectUsecase.getRecord(asyncUnitOfWork, page)

    result = list(map(RecordResponseMapper.entityToResponse, records))
    return result


@router.get("/api/v1/totalPage")
async def totalPage():
    asyncUnitOfWork = injector.get(AbstractUnitOfWork)
    totalPage = await detectUsecase.getTotalPage(asyncUnitOfWork)

    return JSONResponse(
        content={"code": 200, "message": "success", "data": {"totalPage": totalPage}}
    )

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from usecases.fetch_usescases import FetchUseCases
from shared.utils.logger import Logger

router = APIRouter()
fetchUseCases = FetchUseCases()
logger = Logger.getLogger()

@router.get("/fetch")
async def fetch():
    try:
        logger.info("#get_router - fetch - fetching data")
        return await fetchUseCases()
    except Exception as e:
        logger.error(f"#get_router - fetch - error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"code": 500, "message": "Internal Server Error", "data": str(e)},
        )
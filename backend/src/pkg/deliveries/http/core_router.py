__doc__ = """
"""

from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import UploadFile, File

from usecases.core_usecases import CoreUseCases
from shared.utils.logger import Logger

coreUsecases = CoreUseCases()
logger = Logger.getLogger()

router = APIRouter()


@router.post("/core")
async def core(img: UploadFile = File(...)):
    """
    This module defines the core router for handling HTTP POST requests to the "/core" endpoint.

    core(img: UploadFile = File(...)):
        Handles the POST request to the "/core" endpoint. It reads the uploaded image file,
        processes it to count the number of persons in the image, and returns a JSON response
        with the count and the processed image.

        Parameters:
            img (UploadFile): The uploaded image file.

        Returns:
            JSONResponse: A JSON response containing the status code, message, and data
            (person count and processed image) or an error message in case of an exception.
    """
    try:
        return await coreUsecases(img)

    except Exception as e:
        logger.error(f"#core_router - core - error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"code": 500, "message": "Internal Server Error", "data": str(e)},
        )

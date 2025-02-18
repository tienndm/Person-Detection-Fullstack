from fastapi.responses import JSONResponse
from pkg.repositories.postgre.core_manager import CoreManager

from shared.config.postgre import PostgreConf

class FetchUseCases:
    def __init__(self):
        self.coreManager = CoreManager(
            host=PostgreConf.host,
            port=PostgreConf.port,
            user=PostgreConf.user,
            password=PostgreConf.pwd,
            dbname=PostgreConf.db
        )

    async def __call__(self):
        data = self.coreManager.fetch()
        return JSONResponse(
            status_code=200,
            content={"code": 200, "message": "Success", "data": data},
        )

import uvicorn

from fastapi import FastAPI

from pkg.deliveries.http.core_router import router as core_router

app = FastAPI()

app.include_router(core_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

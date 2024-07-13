from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apis.base import api_router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=settings.OPENAPI_URL if settings.HIDE_DOCS == "False" else None,
    docs_url=settings.DOCS_URL if settings.HIDE_DOCS == "False" else None,
    redoc_url=settings.REDOC_URL if settings.HIDE_DOCS == "False" else None,
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)

from fastapi import APIRouter, Depends
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from apis.auth import get_current_token

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello"}

@router.get("/docs", include_in_schema=False)
async def get_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@router.get("/redoc", include_in_schema=False)
async def get_redoc():
    return get_redoc_html(openapi_url="/openapi.json", title="redoc")

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.get("/protected-ping")
async def protected_ping(token: str = Depends(get_current_token)):
    return {"message": "pong"}

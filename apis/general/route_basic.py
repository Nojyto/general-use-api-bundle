from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from apis.auth import get_current_token

router = APIRouter()

@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('static/favicon.ico')

@router.get("/")
async def root():
    return {"message": "Hello"}

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.get("/protected-ping")
async def protected_ping(token: str = Depends(get_current_token)):
    return {"message": "pong"}

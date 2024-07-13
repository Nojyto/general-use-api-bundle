from fastapi import APIRouter
from backend.apis import auth


api_router = APIRouter()
api_router.include_router(auth.router, prefix="", tags=["login"])

from fastapi import APIRouter
from apis.general import route_basic
from apis import auth

api_router = APIRouter()
api_router.include_router(route_basic.router, prefix="", tags=["basic"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

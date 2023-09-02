from fastapi import APIRouter

from app.api.v1.endpoints import user
from app.api.v1.endpoints import ping

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(ping.router, prefix="/ping", tags=["ping"])

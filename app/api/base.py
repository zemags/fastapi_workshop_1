from api.version1 import route_owners, route_arts
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(
    route_owners.router, prefix="/owners", tags=["owners"])
api_router.include_router(
    route_arts.router, prefix="/art", tags=["Arts"])

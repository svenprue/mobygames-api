from fastapi import APIRouter

from app.api.endpoints import games, developers, companies, groups, critics

api_router = APIRouter()
api_router.include_router(games.router, prefix="/games", tags=["games"])
api_router.include_router(developers.router, prefix="/developers", tags=["developers"])
api_router.include_router(companies.router, prefix="/companies", tags=["companies"])
api_router.include_router(groups.router, prefix="/groups", tags=["groups"])
api_router.include_router(critics.router, prefix="/critics", tags=["critics"])
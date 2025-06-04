from fastapi import APIRouter

from app.api.endpoints import games, players, companies, groups, critics

api_router = APIRouter()
api_router.include_router(games.router, prefix="/games", tags=["games"])
api_router.include_router(players.router, prefix="/players", tags=["players"])
api_router.include_router(companies.router, prefix="/companies", tags=["companies"])
api_router.include_router(groups.router, prefix="/groups", tags=["groups"])
api_router.include_router(critics.router, prefix="/critics", tags=["critics"])

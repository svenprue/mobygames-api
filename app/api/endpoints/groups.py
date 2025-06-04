from typing import Optional

from fastapi import APIRouter

from app.schemas import groups as schemas
from app.services.groups.search import MobyGamesGroupSearch
from app.services.groups.profile import MobyGamesGroupProfile
from app.services.groups.games import MobyGamesGroupGames
from app.services.groups.trivia import MobyGamesGroupTrivia

router = APIRouter()


@router.get("/search/{group_name}", response_model=schemas.GroupSearch, response_model_exclude_none=True)
def search_groups(group_name: str, page_number: Optional[int] = 1):
    moby = MobyGamesGroupSearch(query=group_name, page_number=page_number)
    found_groups = moby.search_groups()
    return found_groups


@router.get("/{group_id}/profile", response_model=schemas.GroupProfile, response_model_exclude_defaults=True)
def get_group_profile(group_id: str):
    moby = MobyGamesGroupProfile(group_id=group_id)
    group_profile = moby.get_group_profile()
    return group_profile


@router.get("/{group_id}/games", response_model=schemas.GroupGames, response_model_exclude_defaults=True)
def get_group_games(group_id: str, page_number: Optional[int] = 1):
    moby = MobyGamesGroupGames(group_id=group_id, page_number=page_number)
    group_games = moby.get_group_games()
    return group_games


@router.get("/{group_id}/trivia", response_model=schemas.GroupTrivia, response_model_exclude_defaults=True)
def get_group_trivia(group_id: str):
    moby = MobyGamesGroupTrivia(group_id=group_id)
    trivia = moby.get_group_trivia()
    return trivia
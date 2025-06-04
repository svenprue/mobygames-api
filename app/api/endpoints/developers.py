from typing import Optional

from fastapi import APIRouter

from app.schemas import developers as schemas
from app.services.developers.search import MobyGamesDeveloperSearch
from app.services.developers.profile import MobyGamesDeveloperProfile
from app.services.developers.games import MobyGamesDeveloperGames

router = APIRouter()


@router.get("/search/{developer_name}", response_model=schemas.DeveloperSearch, response_model_exclude_none=True)
def search_developers(developer_name: str, page_number: Optional[int] = 1):
    moby = MobyGamesDeveloperSearch(query=developer_name, page_number=page_number)
    found_developers = moby.search_developers()
    return found_developers


@router.get("/{developer_id}/profile", response_model=schemas.DeveloperProfile, response_model_exclude_defaults=True)
def get_developer_profile(developer_id: str):
    moby = MobyGamesDeveloperProfile(developer_id=developer_id)
    developer_profile = moby.get_developer_profile()
    return developer_profile


@router.get("/{developer_id}/games", response_model=schemas.DeveloperGames, response_model_exclude_defaults=True)
def get_developer_games(developer_id: str, page_number: Optional[int] = 1):
    moby = MobyGamesDeveloperGames(developer_id=developer_id, page_number=page_number)
    developer_games = moby.get_developer_games()
    return developer_games
from typing import Optional

from fastapi import APIRouter

from app.schemas import games as schemas
from app.services.games.search import MobyGamesGameSearch
from app.services.games.profile import MobyGamesGameProfile
from app.services.games.screenshots import MobyGamesGameScreenshots
from app.services.games.credits import MobyGamesGameCredits

router = APIRouter()


@router.get("/search/{game_name}", response_model=schemas.GameSearch, response_model_exclude_none=True)
def search_games(game_name: str, page_number: Optional[int] = 1):
    moby = MobyGamesGameSearch(query=game_name, page_number=page_number)
    found_games = moby.search_games()
    return found_games


@router.get("/{game_id}/profile", response_model=schemas.GameProfile, response_model_exclude_defaults=True)
def get_game_profile(game_id: str):
    moby = MobyGamesGameProfile(game_id=game_id)
    game_profile = moby.get_game_profile()
    return game_profile


@router.get("/{game_id}/screenshots", response_model=schemas.GameScreenshots, response_model_exclude_defaults=True)
def get_game_screenshots(game_id: str):
    moby = MobyGamesGameScreenshots(game_id=game_id)
    screenshots = moby.get_game_screenshots()
    return screenshots


@router.get("/{game_id}/credits", response_model=schemas.GameCredits, response_model_exclude_defaults=True)
def get_game_credits(game_id: str):
    moby = MobyGamesGameCredits(game_id=game_id)
    credits = moby.get_game_credits()
    return credits

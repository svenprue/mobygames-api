from typing import Optional

from fastapi import APIRouter

from app.schemas import companies as schemas
from app.services.companies.search import MobyGamesCompanySearch
from app.services.companies.profile import MobyGamesCompanyProfile
from app.services.companies.games import MobyGamesCompanyGames
from app.services.companies.trivia import MobyGamesCompanyTrivia
from app.services.companies.history import MobyGamesCompanyHistory

router = APIRouter()


@router.get("/search/{company_name}", response_model=schemas.CompanySearch, response_model_exclude_none=True)
def search_companies(company_name: str, page_number: Optional[int] = 1):
    moby = MobyGamesCompanySearch(query=company_name, page_number=page_number)
    found_companies = moby.search_companies()
    return found_companies


@router.get("/{company_id}/profile", response_model=schemas.CompanyProfile, response_model_exclude_defaults=True)
def get_company_profile(company_id: str):
    moby = MobyGamesCompanyProfile(company_id=company_id)
    company_profile = moby.get_company_profile()
    return company_profile


@router.get("/{company_id}/games", response_model=schemas.CompanyGames, response_model_exclude_defaults=True)
def get_company_games(company_id: str, page_number: Optional[int] = 1):
    moby = MobyGamesCompanyGames(company_id=company_id, page_number=page_number)
    company_games = moby.get_company_games()
    return company_games


@router.get("/{company_id}/trivia", response_model=schemas.CompanyTrivia, response_model_exclude_defaults=True)
def get_company_trivia(company_id: str):
    moby = MobyGamesCompanyTrivia(company_id=company_id)
    trivia = moby.get_company_trivia()
    return trivia


@router.get("/{company_id}/history", response_model=schemas.CompanyHistory, response_model_exclude_defaults=True)
def get_company_history(company_id: str):
    moby = MobyGamesCompanyHistory(company_id=company_id)
    history = moby.get_company_history()
    return history
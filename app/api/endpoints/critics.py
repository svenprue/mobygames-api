from typing import Optional

from fastapi import APIRouter

from app.schemas import critics as schemas
from app.services.critics.search import MobyGamesCriticSearch
from app.services.critics.profile import MobyGamesCriticProfile
from app.services.critics.reviews import MobyGamesCriticReviews

router = APIRouter()


@router.get("/search/{critic_name}", response_model=schemas.CriticSearch, response_model_exclude_none=True)
def search_critics(critic_name: str, page_number: Optional[int] = 1):
    moby = MobyGamesCriticSearch(query=critic_name, page_number=page_number)
    found_critics = moby.search_critics()
    return found_critics


@router.get("/{critic_id}/profile", response_model=schemas.CriticProfile, response_model_exclude_defaults=True)
def get_critic_profile(critic_id: str):
    moby = MobyGamesCriticProfile(critic_id=critic_id)
    critic_profile = moby.get_critic_profile()
    return critic_profile


@router.get("/{critic_id}/reviews", response_model=schemas.CriticReviews, response_model_exclude_defaults=True)
def get_critic_reviews(critic_id: str, page_number: Optional[int] = 1):
    moby = MobyGamesCriticReviews(critic_id=critic_id, page_number=page_number)
    critic_reviews = moby.get_critic_reviews()
    return critic_reviews

from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class CriticBase(BaseModel):
    name: str
    url: HttpUrl
    id: str


class CriticSearchResult(CriticBase):
    details: Optional[str] = None


class CriticSearch(BaseModel):
    query: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[CriticSearchResult]


class CriticProfile(CriticBase):
    bio: Optional[str] = None
    website: Optional[HttpUrl] = None
    publication: Optional[str] = None
    specialization: Optional[List[str]] = None


class CriticReview(BaseModel):
    game_title: str
    game_url: HttpUrl
    game_id: str
    date: Optional[str] = None
    score: Optional[str] = None
    text: Optional[str] = None


class CriticReviews(BaseModel):
    critic_id: str
    critic_name: str
    page_number: int
    total_pages: int
    reviews: List[CriticReview]


# New models for missing data
class CriticStats(BaseModel):
    critic_id: str
    critic_name: str
    total_reviews: Optional[int] = None
    average_score: Optional[float] = None
    review_score_distribution: Optional[dict] = None
    most_reviewed_genres: Optional[List[str]] = None
    active_years: Optional[str] = None
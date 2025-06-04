from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class GameBase(BaseModel):
    name: str
    url: HttpUrl
    id: str


class GameSearchResult(GameBase):
    platforms: Optional[List[str]] = None
    year: Optional[int] = None


class GameBrowseResult(GameBase):
    year: Optional[int] = None
    company: Optional[str] = None


class GameSearch(BaseModel):
    query: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[GameSearchResult]


class GameBrowse(BaseModel):
    sort_by: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[GameBrowseResult]


class GamePlatform(BaseModel):
    name: str
    url: Optional[HttpUrl] = None


class GameDeveloper(BaseModel):
    name: str
    url: Optional[HttpUrl] = None


class GamePublisher(BaseModel):
    name: str
    url: Optional[HttpUrl] = None


class GameProfile(GameBase):
    platforms: List[GamePlatform]
    genres: List[str] 
    description: Optional[str] = None
    release_date: Optional[str] = None
    developers: List[GameDeveloper]
    publishers: List[GamePublisher]
    moby_score: Optional[float] = None
    moby_rank: Optional[float] = None
    player_count: Optional[str] = None


class GameScreenshot(BaseModel):
    url: HttpUrl
    caption: Optional[str] = None


class GameScreenshots(BaseModel):
    game_id: str
    game_name: str
    screenshots: List[GameScreenshot]


class GameCreditPerson(BaseModel):
    name: str
    url: HttpUrl
    id: str


class GameCreditGroup(BaseModel):
    group_name: str
    roles: List[str]
    people: List[GameCreditPerson]


class GameCredits(BaseModel):
    game_id: str
    game_name: str
    credits: List[GameCreditGroup]


# New models for missing data
class GameTechSpec(BaseModel):
    category: str
    attribute: str
    value: str


class GameSpecs(BaseModel):
    game_id: str
    game_name: str
    platform: Optional[str] = None
    minimum_requirements: List[GameTechSpec] = []
    recommended_requirements: List[GameTechSpec] = []
    technical_attributes: List[GameTechSpec] = []


class GameRating(BaseModel):
    rating_system: str
    rating: str
    content_descriptors: Optional[List[str]] = None


class GameReview(BaseModel):
    reviewer_name: str
    publication: Optional[str] = None
    score: Optional[str] = None
    max_score: Optional[str] = None
    review_text: Optional[str] = None
    review_date: Optional[str] = None
    url: Optional[HttpUrl] = None


class GameRatings(BaseModel):
    game_id: str
    game_name: str
    moby_score: Optional[float] = None
    moby_rank: Optional[float] = None
    user_rating: Optional[float] = None
    critic_rating: Optional[float] = None
    age_ratings: List[GameRating] = []
    reviews: List[GameReview] = []


class GameTrivia(BaseModel):
    game_id: str
    game_name: str
    trivia_entries: List[str] = []


class GameRelease(BaseModel):
    platform: str
    region: str
    release_date: Optional[str] = None
    publisher: Optional[str] = None
    developer: Optional[str] = None
    product_code: Optional[str] = None
    age_rating: Optional[str] = None


class GameReleases(BaseModel):
    game_id: str
    game_name: str
    releases: List[GameRelease] = []
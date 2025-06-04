from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class GameBase(BaseModel):
    name: str
    url: HttpUrl
    id: str


class GameSearchResult(GameBase):
    platforms: Optional[List[str]] = None
    year: Optional[int] = None


class GameSearch(BaseModel):
    query: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[GameSearchResult]


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

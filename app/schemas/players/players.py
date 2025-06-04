from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class PlayerBase(BaseModel):
    name: str
    url: HttpUrl
    id: str


class PlayerSearchResult(PlayerBase):
    games_count: Optional[int] = None


class PlayerSearch(BaseModel):
    query: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[PlayerSearchResult]


class PlayerProfile(PlayerBase):
    bio: Optional[str] = None
    known_aliases: Optional[List[str]] = None


class PlayerCreditGame(BaseModel):
    title: str
    url: HttpUrl
    id: str
    roles: List[str]


class PlayerCredits(BaseModel):
    player_id: str
    player_name: str
    credits: List[PlayerCreditGame]

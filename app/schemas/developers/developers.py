from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class DeveloperBase(BaseModel):
    name: str
    url: HttpUrl
    id: str


class DeveloperSearchResult(DeveloperBase):
    games_count: Optional[int] = None


class DeveloperSearch(BaseModel):
    query: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[DeveloperSearchResult]


class DeveloperProfile(DeveloperBase):
    bio: Optional[str] = None
    known_aliases: Optional[List[str]] = None


class DeveloperCreditGame(BaseModel):
    title: str
    url: HttpUrl
    id: str
    platforms: List[str]
    year: Optional[int] = None
    role: str


class DeveloperGames(BaseModel):
    developer_id: str
    developer_name: str
    page_number: int
    total_pages: int
    games: List[DeveloperCreditGame]
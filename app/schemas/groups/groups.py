from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class GroupBase(BaseModel):
    name: str
    url: HttpUrl
    id: str


class GroupSearchResult(GroupBase):
    details: Optional[str] = None


class GroupSearch(BaseModel):
    query: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[GroupSearchResult]


class GroupMember(BaseModel):
    name: str
    url: HttpUrl
    id: str


class GroupProfile(GroupBase):
    description: Optional[str] = None
    members: List[GroupMember]


class GroupGame(BaseModel):
    title: str
    url: HttpUrl
    id: str
    platforms: List[str]
    year: Optional[int] = None


class GroupGames(BaseModel):
    group_id: str
    group_name: str
    page_number: int
    total_pages: int
    games: List[GroupGame]

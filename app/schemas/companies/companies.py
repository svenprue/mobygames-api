from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class CompanyBase(BaseModel):
    name: str
    url: HttpUrl
    id: str


class CompanySearchResult(CompanyBase):
    games_count: Optional[int] = None


class CompanySearch(BaseModel):
    query: str
    page_number: int
    total_results: int
    total_pages: int
    results: List[CompanySearchResult]


class CompanyProfile(CompanyBase):
    overview: Optional[str] = None
    founded: Optional[str] = None
    website: Optional[HttpUrl] = None
    headquarters: Optional[str] = None
    status: Optional[str] = None  # Active, Defunct, etc.
    parent_company: Optional[str] = None
    employee_count: Optional[str] = None


class CompanyGame(BaseModel):
    title: str
    url: HttpUrl
    id: str
    platforms: List[str]
    year: Optional[int] = None
    role: str  # Developer, Publisher, etc.


class CompanyGames(BaseModel):
    company_id: str
    company_name: str
    page_number: int
    total_pages: int
    games: List[CompanyGame]


# New models for missing data
class CompanyTrivia(BaseModel):
    company_id: str
    company_name: str
    trivia_entries: List[str] = []


class CompanyHistoryEntry(BaseModel):
    date: Optional[str] = None
    event: str


class CompanyHistory(BaseModel):
    company_id: str
    company_name: str
    history_entries: List[CompanyHistoryEntry] = []
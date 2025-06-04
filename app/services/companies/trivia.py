from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Companies


class MobyGamesCompanyTrivia(BaseScraper):
    def __init__(self, company_id: str):
        super().__init__()
        self.company_id = company_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/company/{self.company_id}/trivia"

    def get_company_trivia(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get company name for reference
        company_name = self._get_text(response.xpath(Companies.NAME))

        # Extract trivia entries
        trivia_entries = self._extract_trivia_entries(response)

        return {
            "company_id": self.company_id,
            "company_name": company_name,
            "trivia_entries": trivia_entries
        }

    def _extract_trivia_entries(self, response) -> List[str]:
        trivia_entries = []

        # Extract trivia from the page
        trivia_elements = response.xpath(Companies.TRIVIA_ENTRIES)

        for element in trivia_elements:
            trivia_text = self._clean_text(element)
            if trivia_text:
                trivia_entries.append(trivia_text)

        return trivia_entries
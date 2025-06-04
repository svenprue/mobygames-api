from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Developers


class MobyGamesDeveloperTrivia(BaseScraper):
    def __init__(self, developer_id: str):
        super().__init__()
        self.developer_id = developer_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/developer/{self.developer_id}/trivia"

    def get_developer_trivia(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get developer name for reference
        developer_name = self._get_text(response.xpath(Developers.NAME))

        # Extract trivia entries
        trivia_entries = self._extract_trivia_entries(response)

        return {
            "developer_id": self.developer_id,
            "developer_name": developer_name,
            "trivia_entries": trivia_entries
        }

    def _extract_trivia_entries(self, response) -> List[str]:
        trivia_entries = []

        # Extract trivia from the page
        trivia_elements = response.xpath(Developers.TRIVIA_ENTRIES)

        for element in trivia_elements:
            trivia_text = self._clean_text(element)
            if trivia_text:
                trivia_entries.append(trivia_text)

        return trivia_entries
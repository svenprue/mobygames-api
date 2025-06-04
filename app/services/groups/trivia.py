from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Groups


class MobyGamesGroupTrivia(BaseScraper):
    def __init__(self, group_id: str):
        super().__init__()
        self.group_id = group_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/group/{self.group_id}/trivia"

    def get_group_trivia(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get group name for reference
        group_name = self._get_text(response.xpath(Groups.NAME))

        # Extract trivia entries
        trivia_entries = self._extract_trivia_entries(response)

        return {
            "group_id": self.group_id,
            "group_name": group_name,
            "trivia_entries": trivia_entries
        }

    def _extract_trivia_entries(self, response) -> List[str]:
        trivia_entries = []

        # Extract trivia from the page
        trivia_elements = response.xpath(Groups.TRIVIA_ENTRIES)

        for element in trivia_elements:
            trivia_text = self._clean_text(element)
            if trivia_text:
                trivia_entries.append(trivia_text)

        return trivia_entries
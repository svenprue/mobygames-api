from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameTrivia(BaseScraper):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/game/{self.game_id}/trivia"

    def get_game_trivia(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get game name for reference
        game_name = self._get_text(response.xpath(Games.TITLE))

        # Extract trivia entries
        trivia_entries = self._extract_trivia_entries(response)

        return {
            "game_id": self.game_id,
            "game_name": game_name,
            "trivia_entries": trivia_entries
        }

    def _extract_trivia_entries(self, response) -> List[str]:
        trivia_entries = []

        # Extract trivia from the page
        trivia_elements = response.xpath(Games.TRIVIA_ENTRIES)

        for element in trivia_elements:
            trivia_text = self._clean_text(element)
            if trivia_text:
                trivia_entries.append(trivia_text)

        return trivia_entries
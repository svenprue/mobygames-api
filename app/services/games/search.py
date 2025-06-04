import re
from typing import Dict, List, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameSearch(BaseScraper):
    def __init__(self, query: str, page_number: int = 1):
        super().__init__()
        self.query = query
        self.page_number = page_number
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        # Build the search URL with query and pagination
        return f"{self.base_url}/search/games?q={self.query}&p={self.page_number}"

    def search_games(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Parse search results
        search_results = response.xpath(Games.SEARCH_RESULTS)
        results = []

        for result in search_results:
            name = self._get_text(result.xpath(Games.GAME_NAME))
            url_path = self._get_text(result.xpath(Games.GAME_URL))
            game_id = self._extract_id_from_url(url_path)

            platforms = result.xpath(Games.GAME_PLATFORMS)
            platforms_list = [platform.strip() for platform in platforms if platform.strip()]

            year_text = self._get_text(result.xpath(Games.GAME_YEAR))
            year = self._extract_year(year_text)

            results.append({
                "name": name,
                "url": f"{self.base_url}{url_path}",
                "id": game_id,
                "platforms": platforms_list,
                "year": year
            })

        # Get pagination info
        total_results = len(results)
        total_pages = 1

        # Look for pagination info in the page
        pagination_text = self._get_text(response.xpath("//div[@class='pagination']/text()"))
        if pagination_text:
            match = re.search(r'of (\d+)', pagination_text)
            if match:
                total_pages = int(match.group(1))

        return {
            "query": self.query,
            "page_number": self.page_number,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }

    def _extract_id_from_url(self, url: str) -> str:
        # Extract game ID from URL
        match = re.search(r'/game/(\d+)/', url)
        if match:
            return match.group(1)
        return ""

    def _extract_year(self, text: str) -> Optional[int]:
        # Extract year from text like " (1998)"
        if text:
            match = re.search(r'\((\d{4})\)', text)
            if match:
                return int(match.group(1))
        return None

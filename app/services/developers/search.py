import re
from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Developers


class MobyGamesDeveloperSearch(BaseScraper):
    def __init__(self, query: str, page_number: int = 1):
        super().__init__()
        self.query = query
        self.page_number = page_number
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        # Build the search URL with query and pagination
        return f"{self.base_url}/search/developers?q={self.query}&p={self.page_number}"

    def search_developers(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Parse search results
        search_results = response.xpath(Developers.SEARCH_RESULTS)
        results = []

        for result in search_results:
            name = self._get_text(result.xpath(Developers.DEVELOPER_NAME))
            url_path = self._get_text(result.xpath(Developers.DEVELOPER_URL))
            developer_id = self._extract_id_from_url(url_path)

            games_count_text = self._get_text(result.xpath(Developers.DEVELOPER_GAMES_COUNT))
            games_count = self._extract_games_count(games_count_text)

            results.append({
                "name": name,
                "url": f"{self.base_url}{url_path}",
                "id": developer_id,
                "games_count": games_count
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
        # Extract developer ID from URL
        match = re.search(r'/developer/(\d+)/', url)
        if match:
            return match.group(1)
        return ""

    def _extract_games_count(self, text: str) -> int:
        # Extract games count from text like "Involved in 42 games"
        if text:
            match = re.search(r'Involved in (\d+) games', text)
            if match:
                return int(match.group(1))
        return 0
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
        # Use the actual MobyGames search URL format
        return f"{self.base_url}/search/?q={self.query}&type=game&p={self.page_number}"

    def search_games(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Parse search results from the table structure
        search_results = response.xpath(Games.SEARCH_RESULTS)
        results = []

        for result in search_results:
            # Extract game name from the bold link
            name_element = result.xpath(Games.GAME_NAME)
            name = self._get_text(name_element) if name_element else ""

            # Extract game URL
            url_element = result.xpath(Games.GAME_URL)
            url_path = url_element[0] if url_element else ""

            # Extract game ID from URL
            game_id = self._extract_id_from_url(url_path)

            # Extract platforms and year from the second column
            platforms_and_year = result.xpath(Games.GAME_PLATFORMS_AND_YEAR)
            platforms, year = self._parse_platforms_and_year(platforms_and_year)

            if name and url_path:  # Only add if we have essential data
                results.append({
                    "name": name,
                    "url": url_path if url_path.startswith('http') else f"{self.base_url}{url_path}",
                    "id": game_id,
                    "platforms": platforms,
                    "year": year
                })

        # Get pagination info - MobyGames uses different pagination
        total_results = len(results)
        total_pages = self._extract_total_pages(response)

        return {
            "query": self.query,
            "page_number": self.page_number,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }

    def _extract_id_from_url(self, url: str) -> str:
        """Extract game ID from URL like /game/12345/game-name"""
        if not url:
            return ""
        match = re.search(r'/game/(\d+)/', url)
        return match.group(1) if match else ""

    def _parse_platforms_and_year(self, elements: List) -> tuple:
        """Parse platforms and year from the HTML elements"""
        platforms = []
        year = None

        for element in elements:
            text = element.strip() if isinstance(element, str) else ""

            # Look for year in parentheses like "(March 29, 1996)" or "(1996)"
            year_match = re.search(r'\(.*?(\d{4})\)', text)
            if year_match:
                year = int(year_match.group(1))

            # Look for platform names (usually before the year)
            # This is simplified - might need refinement based on actual HTML structure
            if text and not re.search(r'\(\d{4}\)', text) and len(text) < 20:
                platforms.append(text)

        return platforms, year

    def _extract_total_pages(self, response) -> int:
        """Extract total number of pages from pagination"""
        # Look for pagination links or text
        pagination_elements = response.xpath("//div[@class='pagination']//text() | //nav[@class='pagination']//text()")

        for element in pagination_elements:
            # Look for pattern like "Page 1 of 25"
            match = re.search(r'of (\d+)', element)
            if match:
                return int(match.group(1))

        return 1  # Default to 1 page if pagination not found
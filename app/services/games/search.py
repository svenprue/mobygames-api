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
        # Use the actual MobyGames search URL format with 'page' instead of 'p'
        return f"{self.base_url}/search/?q={self.query}&type=game&page={self.page_number}"

    def search_games(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Extract total results from the results info paragraph
        total_results = self._extract_total_results(response)

        # Parse search results from the table structure
        search_results = response.xpath(Games.SEARCH_RESULTS)
        results = []

        for result in search_results:
            # Extract game name from the bold link in second td
            name_elements = result.xpath(Games.GAME_NAME)
            name = name_elements[0] if name_elements else ""

            # Extract game URL
            url_elements = result.xpath(Games.GAME_URL)
            url_path = url_elements[0] if url_elements else ""

            # Extract game ID from URL
            game_id = self._extract_id_from_url(url_path)

            # Extract platforms and year from the second td
            platforms, year = self._parse_platforms_and_year(result)

            if name and url_path:  # Only add if we have essential data
                results.append({
                    "name": name,
                    "url": url_path if url_path.startswith('http') else f"{self.base_url}{url_path}",
                    "id": game_id,
                    "platforms": platforms,
                    "year": year
                })

        # Extract pagination info
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

    def _parse_platforms_and_year(self, row_element) -> tuple:
        """Parse platforms and year from the table row's second td"""
        platforms = []
        year = None

        # Get all text from the second td
        second_td = row_element.xpath('.//td[2]')[0] if row_element.xpath('.//td[2]') else None
        if not second_td:
            return platforms, year

        # Extract year from the date span like "(December 6, 2019)"
        date_spans = second_td.xpath('.//span[@class="text-muted"][contains(text(), "(")]')
        for span in date_spans:
            date_text = span.text or ""
            year_match = re.search(r'\(.*?(\d{4})\)', date_text)
            if year_match:
                year = int(year_match.group(1))
                break

        # Extract platforms from the small tags (excluding the year info)
        platform_elements = second_td.xpath(
            './/small[position()=last()]//text()[not(ancestor::small[@class="text-muted"])]')
        for platform_text in platform_elements:
            platform_text = platform_text.strip()
            # Skip empty strings and year info
            if platform_text and not re.search(r'\(\d{4}\)', platform_text) and platform_text != ',':
                platforms.append(platform_text)

        return platforms, year

    def _extract_total_results(self, response) -> int:
        """Extract total number of results from the results info paragraph"""
        # Look for text like "1,492 results for"
        results_info = response.xpath('//p[@class="text-sm"]//text()')
        for text in results_info:
            match = re.search(r'([\d,]+)\s+results?\s+for', text)
            if match:
                # Remove commas and convert to int
                return int(match.group(1).replace(',', ''))
        return len(response.xpath(Games.SEARCH_RESULTS))

    def _extract_total_pages(self, response) -> int:
        """Extract total number of pages from pagination"""
        # Look for pagination text like "Page 2 of 125"
        pagination_elements = response.xpath('//div[@class="mb"]//text()')

        for element in pagination_elements:
            # Look for pattern like "Page X of Y"
            match = re.search(r'Page\s+\d+\s+of\s+(\d+)', element)
            if match:
                return int(match.group(1))

        return 1  # Default to 1 page if pagination not found
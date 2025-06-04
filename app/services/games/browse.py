import re
from typing import Dict, List, Optional

from app.services.base import BaseScraper


class MobyGamesGameBrowse(BaseScraper):
    def __init__(self, page_number: int = 1, sort_by: str = "date"):
        super().__init__()
        self.page_number = page_number
        self.sort_by = sort_by
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        # Use the MobyGames browse URL format
        return f"{self.base_url}/game/sort:{self.sort_by}/page:{self.page_number}/"

    def browse_games(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Extract total results and pages from pagination info
        total_results, total_pages = self._extract_pagination_info(response)

        # Parse browse results from the table structure
        browse_results = response.xpath("//table[@class='table table-hover mb']//tr[td]")
        results = []

        for result in browse_results:
            # Extract game name from the first td
            name_elements = result.xpath('.//td[1]//a[contains(@href, "/game/")]/text()')
            name = name_elements[0] if name_elements else ""

            # Extract game URL
            url_elements = result.xpath('.//td[1]//a[contains(@href, "/game/")]/@href')
            url_path = url_elements[0] if url_elements else ""

            # Extract game ID from URL
            game_id = self._extract_id_from_url(url_path)

            # Extract year from second td
            year_elements = result.xpath('.//td[2]/text()')
            year = None
            if year_elements:
                year_text = year_elements[0].strip()
                if year_text.isdigit():
                    year = int(year_text)

            # Extract company/developer from third td
            company_elements = result.xpath('.//td[3]/text()')
            company = company_elements[0].strip() if company_elements else ""

            if name and url_path:  # Only add if we have essential data
                results.append({
                    "name": name,
                    "url": url_path if url_path.startswith('http') else f"{self.base_url}{url_path}",
                    "id": game_id,
                    "year": year,
                    "company": company
                })

        return {
            "sort_by": self.sort_by,
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

    def _extract_pagination_info(self, response) -> tuple:
        """Extract total results and pages from pagination info"""
        total_results = 0
        total_pages = 1

        # Look for pagination text like "[ Page 1 of 2939 ] [ 146,911 results ]"
        pagination_text = response.xpath('//p[@class="no-select text-muted"]//text()')

        for text in pagination_text:
            text = text.strip()
            # Look for "Page X of Y"
            page_match = re.search(r'Page\s+\d+\s+of\s+([\d,]+)', text)
            if page_match:
                total_pages = int(page_match.group(1).replace(',', ''))

            # Look for "X results"
            results_match = re.search(r'([\d,]+)\s+results', text)
            if results_match:
                total_results = int(results_match.group(1).replace(',', ''))

        return total_results, total_pages
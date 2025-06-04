import re
from typing import Dict, List, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Companies


class MobyGamesCompanyGames(BaseScraper):
    def __init__(self, company_id: str, page_number: int = 1):
        super().__init__()
        self.company_id = company_id
        self.page_number = page_number
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/company/{self.company_id}/games?page={self.page_number}"

    def get_company_games(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get company name for reference
        company_name = self._get_text(response.xpath(Companies.NAME))

        # Extract games section
        games_section = response.xpath(Companies.GAMES_SECTION)

        # Get game entries
        game_entries = games_section.xpath(Companies.GAME_ENTRIES)
        games = []

        for game_entry in game_entries:
            # Extract game info
            game_title = self._get_text(game_entry.xpath(Companies.GAME_TITLE))
            game_url_path = self._get_text(game_entry.xpath(Companies.GAME_URL))

            # Extract platforms
            platform_elements = game_entry.xpath(Companies.GAME_PLATFORMS)
            platforms = [platform.strip() for platform in platform_elements if platform.strip()]

            # Extract year
            year_text = self._get_text(game_entry.xpath(Companies.GAME_YEAR))
            year = self._extract_year(year_text)

            # Extract role (developer, publisher, etc.)
            role = self._get_text(game_entry.xpath(Companies.GAME_ROLE))

            # Extract game ID from URL
            game_id = ""
            if game_url_path:
                match = re.search(r'/game/(\d+)/', game_url_path)
                if match:
                    game_id = match.group(1)

            games.append({
                "title": game_title,
                "url": f"{self.base_url}{game_url_path}" if game_url_path else "",
                "id": game_id,
                "platforms": platforms,
                "year": year,
                "role": role
            })

        # Get pagination info
        total_pages = 1

        # Look for pagination info in the page
        pagination_text = self._get_text(response.xpath("//div[@class='pagination']/text()"))
        if pagination_text:
            match = re.search(r'of (\d+)', pagination_text)
            if match:
                total_pages = int(match.group(1))

        return {
            "company_id": self.company_id,
            "company_name": company_name,
            "page_number": self.page_number,
            "total_pages": total_pages,
            "games": games
        }

    def _extract_year(self, text: str) -> Optional[int]:
        # Extract year from text
        if text:
            match = re.search(r'(\d{4})', text)
            if match:
                return int(match.group(1))
        return None

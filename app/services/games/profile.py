import re
from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameProfile(BaseScraper):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/game/{self.game_id}"

    def get_game_profile(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Extract basic game info
        title = self._get_text(response.xpath(Games.TITLE))

        # Extract platforms
        platform_elements = response.xpath(Games.PLATFORMS)
        platforms = []
        for platform in platform_elements:
            platform_name = platform.strip()
            platforms.append({
                "name": platform_name,
                "url": f"{self.base_url}/browse/games/platform/{self._format_platform_url(platform_name)}"
            })

        # Extract genres
        genre_elements = response.xpath(Games.GENRES)
        genres = [genre.strip() for genre in genre_elements if genre.strip()]

        # Extract description
        description = self._get_text(response.xpath(Games.DESCRIPTION))

        # Extract release info
        release_date = self._get_text(response.xpath(Games.RELEASE_INFO))

        # Extract developers
        developer_names = response.xpath(Games.DEVELOPER)
        developers = []
        for dev_name in developer_names:
            developers.append({
                "name": dev_name,
                "url": f"{self.base_url}/company/{self._format_company_url(dev_name)}"
            })

        # Extract publishers
        publisher_names = response.xpath(Games.PUBLISHER)
        publishers = []
        for pub_name in publisher_names:
            publishers.append({
                "name": pub_name,
                "url": f"{self.base_url}/company/{self._format_company_url(pub_name)}"
            })

        return {
            "name": title,
            "url": url,
            "id": self.game_id,
            "platforms": platforms,
            "genres": genres,
            "description": description,
            "release_date": release_date,
            "developers": developers,
            "publishers": publishers
        }

    def _format_platform_url(self, platform_name: str) -> str:
        # Format platform name for URL
        return platform_name.lower().replace(' ', '-')

    def _format_company_url(self, company_name: str) -> str:
        # Format company name for URL
        # This is a simplification; actual implementation would need to handle the company ID
        return company_name.lower().replace(' ', '-')

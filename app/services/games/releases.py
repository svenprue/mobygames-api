import re
from typing import Dict, List, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameReleases(BaseScraper):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/game/{self.game_id}/releases"

    def get_game_releases(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get game name for reference
        game_name = self._get_text(response.xpath(Games.TITLE))

        # Extract releases
        releases = self._extract_releases(response)

        return {
            "game_id": self.game_id,
            "game_name": game_name,
            "releases": releases
        }

    def _extract_releases(self, response) -> List[Dict]:
        releases = []

        release_elements = response.xpath(Games.RELEASE_ENTRIES)

        for element in release_elements:
            platform = self._get_text(element.xpath(Games.RELEASE_PLATFORM))
            region = self._get_text(element.xpath(Games.RELEASE_REGION))
            release_date = self._get_text(element.xpath(Games.RELEASE_DATE))
            publisher = self._get_text(element.xpath(Games.RELEASE_PUBLISHER))
            developer = self._get_text(element.xpath(Games.RELEASE_DEVELOPER))
            product_code = self._get_text(element.xpath(Games.RELEASE_PRODUCT_CODE))
            age_rating = self._get_text(element.xpath(Games.RELEASE_AGE_RATING))

            if platform:
                releases.append({
                    "platform": platform,
                    "region": region or "Unknown",
                    "release_date": release_date,
                    "publisher": publisher,
                    "developer": developer,
                    "product_code": product_code,
                    "age_rating": age_rating
                })

        return releases
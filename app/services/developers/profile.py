from typing import Dict, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Developers


class MobyGamesDeveloperProfile(BaseScraper):
    def __init__(self, developer_id: str):
        super().__init__()
        self.developer_id = developer_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/developer/{self.developer_id}"

    def get_developer_profile(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Extract basic developer info
        name = self._get_text(response.xpath(Developers.NAME))

        # Extract bio if available
        bio = self._get_text(response.xpath(Developers.BIO))

        # Extract known aliases if available
        alias_elements = response.xpath(Developers.KNOWN_ALIASES)
        known_aliases = [alias.strip() for alias in alias_elements if alias.strip()]

        result = {
            "name": name,
            "url": url,
            "id": self.developer_id,
            "bio": bio
        }

        if known_aliases:
            result["known_aliases"] = known_aliases

        return result
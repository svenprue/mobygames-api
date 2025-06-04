from typing import Dict, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Critics


class MobyGamesCriticProfile(BaseScraper):
    def __init__(self, critic_id: str):
        super().__init__()
        self.critic_id = critic_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/critic/{self.critic_id}"

    def get_critic_profile(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Extract basic critic info
        name = self._get_text(response.xpath(Critics.NAME))

        # Extract bio if available
        bio = self._get_text(response.xpath(Critics.BIO))

        # Extract website if available
        website_url = self._get_text(response.xpath(Critics.WEBSITE))

        result = {
            "name": name,
            "url": url,
            "id": self.critic_id,
            "bio": bio
        }

        if website_url:
            result["website"] = website_url

        return result

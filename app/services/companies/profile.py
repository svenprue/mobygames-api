from typing import Dict, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Companies


class MobyGamesCompanyProfile(BaseScraper):
    def __init__(self, company_id: str):
        super().__init__()
        self.company_id = company_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/company/{self.company_id}"

    def get_company_profile(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Extract basic company info
        name = self._get_text(response.xpath(Companies.NAME))

        # Extract company overview if available
        overview = self._get_text(response.xpath(Companies.OVERVIEW))

        # Extract founded date if available
        founded = self._get_text(response.xpath(Companies.FOUNDED))

        # Extract website if available
        website_url = self._get_text(response.xpath(Companies.WEBSITE))

        result = {
            "name": name,
            "url": url,
            "id": self.company_id,
            "overview": overview,
            "founded": founded
        }

        if website_url:
            result["website"] = website_url

        return result

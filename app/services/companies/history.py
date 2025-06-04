from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Companies


class MobyGamesCompanyHistory(BaseScraper):
    def __init__(self, company_id: str):
        super().__init__()
        self.company_id = company_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/company/{self.company_id}/history"

    def get_company_history(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get company name for reference
        company_name = self._get_text(response.xpath(Companies.NAME))

        # Extract history entries
        history_entries = self._extract_history_entries(response)

        return {
            "company_id": self.company_id,
            "company_name": company_name,
            "history_entries": history_entries
        }

    def _extract_history_entries(self, response) -> List[Dict]:
        history_entries = []

        # Extract history from the page
        history_elements = response.xpath(Companies.HISTORY_ENTRIES)

        for element in history_elements:
            date = self._get_text(element.xpath(Companies.HISTORY_DATE))
            event = self._get_text(element.xpath(Companies.HISTORY_EVENT))

            if event:
                history_entries.append({
                    "date": date,
                    "event": event
                })

        return history_entries
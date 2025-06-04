import re
from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Critics


class MobyGamesCriticSearch(BaseScraper):
    def __init__(self, query: str, page_number: int = 1):
        super().__init__()
        self.query = query
        self.page_number = page_number
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        # Build the search URL with query and pagination
        return f"{self.base_url}/search/critics?q={self.query}&p={self.page_number}"

    def search_critics(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Parse search results
        search_results = response.xpath(Critics.SEARCH_RESULTS)
        results = []

        for result in search_results:
            name = self._get_text(result.xpath(Critics.CRITIC_NAME))
            url_path = self._get_text(result.xpath(Critics.CRITIC_URL))
            critic_id = self._extract_id_from_url(url_path)

            details = self._get_text(result.xpath(Critics.CRITIC_DETAILS))

            results.append({
                "name": name,
                "url": f"{self.base_url}{url_path}",
                "id": critic_id,
                "details": details
            })

        # Get pagination info
        total_results = len(results)
        total_pages = 1

        # Look for pagination info in the page
        pagination_text = self._get_text(response.xpath("//div[@class='pagination']/text()"))
        if pagination_text:
            match = re.search(r'of (\d+)', pagination_text)
            if match:
                total_pages = int(match.group(1))

        return {
            "query": self.query,
            "page_number": self.page_number,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }

    def _extract_id_from_url(self, url: str) -> str:
        # Extract critic ID from URL
        match = re.search(r'/critic/(\d+)/', url)
        if match:
            return match.group(1)
        return ""

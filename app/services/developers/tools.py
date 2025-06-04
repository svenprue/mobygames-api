from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Developers


class MobyGamesDeveloperTools(BaseScraper):
    def __init__(self, developer_id: str):
        super().__init__()
        self.developer_id = developer_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/developer/{self.developer_id}/tools"

    def get_developer_tools(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get developer name for reference
        developer_name = self._get_text(response.xpath(Developers.NAME))

        # Extract tools
        tools = self._extract_tools(response)

        return {
            "developer_id": self.developer_id,
            "developer_name": developer_name,
            "tools": tools
        }

    def _extract_tools(self, response) -> List[Dict]:
        tools = []

        # Extract tools from the page
        tool_elements = response.xpath(Developers.TOOL_ENTRIES)

        for element in tool_elements:
            name = self._get_text(element.xpath(Developers.TOOL_NAME))
            category = self._get_text(element.xpath(Developers.TOOL_CATEGORY))

            if name:
                tools.append({
                    "name": name,
                    "category": category or "Unknown"
                })

        return tools
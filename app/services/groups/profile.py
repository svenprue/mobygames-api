import re
from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Groups


class MobyGamesGroupProfile(BaseScraper):
    def __init__(self, group_id: str):
        super().__init__()
        self.group_id = group_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/group/{self.group_id}"

    def get_group_profile(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Extract basic group info
        name = self._get_text(response.xpath(Groups.NAME))

        # Extract group description if available
        description = self._get_text(response.xpath(Groups.DESCRIPTION))

        # Extract members
        member_elements = response.xpath(Groups.MEMBERS)
        members = []

        for member_element in member_elements:
            member_name = self._get_text(member_element.xpath(Groups.MEMBER_NAME))
            member_url_path = self._get_text(member_element.xpath(Groups.MEMBER_URL))

            # Extract member ID from URL
            member_id = ""
            if member_url_path:
                match = re.search(r'/person/(\d+)/', member_url_path)
                if match:
                    member_id = match.group(1)

            members.append({
                "name": member_name,
                "url": f"{self.base_url}{member_url_path}" if member_url_path else "",
                "id": member_id
            })

        return {
            "name": name,
            "url": url,
            "id": self.group_id,
            "description": description,
            "members": members
        }

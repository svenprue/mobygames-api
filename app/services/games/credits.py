import re
from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameCredits(BaseScraper):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/game/{self.game_id}/credits"

    def get_game_credits(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get game name for reference
        game_name = self._get_text(response.xpath("//div[@id='gameTitle']/h1/text()"))

        # Extract credits section
        credits_section = response.xpath(Games.CREDITS_SECTION)

        # Get credit groups
        credit_groups_names = credits_section.xpath(Games.CREDIT_GROUPS)

        credits = []
        current_index = 0

        for group_name in credit_groups_names:
            # For each group, find the associated roles and people
            # This is complex and might require navigating between siblings
            # This implementation is simplified and may need adjustment

            # Find the next section with roles and people
            role_names = credits_section.xpath(Games.CREDIT_NAMES)[current_index:]
            people_names = credits_section.xpath(Games.CREDIT_PEOPLE)[current_index:]
            people_urls = credits_section.xpath(Games.CREDIT_PEOPLE_URLS)[current_index:]

            # Count roles for this group
            roles = []
            people = []

            # The number of roles/people will vary for each group
            # This is a simplified approach
            for i in range(len(role_names)):
                if i >= len(people_names):
                    break

                roles.append(role_names[i].strip())

                person_name = people_names[i].strip()
                person_url = people_urls[i] if i < len(people_urls) else ""

                # Extract ID from URL
                person_id = ""
                if person_url:
                    match = re.search(r'/person/(\d+)/', person_url)
                    if match:
                        person_id = match.group(1)

                people.append({
                    "name": person_name,
                    "url": f"{self.base_url}{person_url}" if person_url else "",
                    "id": person_id
                })

            current_index += len(roles)

            credits.append({
                "group_name": group_name.strip(),
                "roles": roles,
                "people": people
            })

        return {
            "game_id": self.game_id,
            "game_name": game_name,
            "credits": credits
        }

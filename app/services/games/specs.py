import re
from typing import Dict, List, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameSpecs(BaseScraper):
    def __init__(self, game_id: str, platform: Optional[str] = None):
        super().__init__()
        self.game_id = game_id
        self.platform = platform
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        if self.platform:
            return f"{self.base_url}/game/{self.game_id}/specs/{self.platform.lower()}"
        return f"{self.base_url}/game/{self.game_id}/specs"

    def get_game_specs(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get game name for reference
        game_name = self._get_text(response.xpath(Games.TITLE))

        # Extract minimum requirements
        minimum_requirements = self._extract_requirements(response, "minimum")

        # Extract recommended requirements
        recommended_requirements = self._extract_requirements(response, "recommended")

        # Extract technical attributes
        technical_attributes = self._extract_technical_attributes(response)

        return {
            "game_id": self.game_id,
            "game_name": game_name,
            "platform": self.platform,
            "minimum_requirements": minimum_requirements,
            "recommended_requirements": recommended_requirements,
            "technical_attributes": technical_attributes
        }

    def _extract_requirements(self, response, req_type: str) -> List[Dict]:
        requirements = []

        # Look for requirement sections
        req_elements = response.xpath(Games.TECH_SPECS_REQUIREMENTS.format(type=req_type))

        for element in req_elements:
            category = self._get_text(element.xpath(Games.SPEC_CATEGORY))
            attribute = self._get_text(element.xpath(Games.SPEC_ATTRIBUTE))
            value = self._get_text(element.xpath(Games.SPEC_VALUE))

            if attribute and value:
                requirements.append({
                    "category": category or "System",
                    "attribute": attribute,
                    "value": value
                })

        return requirements

    def _extract_technical_attributes(self, response) -> List[Dict]:
        attributes = []

        # Extract technical specifications
        attr_elements = response.xpath(Games.TECH_SPECS_ATTRIBUTES)

        for element in attr_elements:
            category = self._get_text(element.xpath(Games.SPEC_CATEGORY))
            attribute = self._get_text(element.xpath(Games.SPEC_ATTRIBUTE))
            value = self._get_text(element.xpath(Games.SPEC_VALUE))

            if attribute and value:
                attributes.append({
                    "category": category or "Technical",
                    "attribute": attribute,
                    "value": value
                })

        return attributes
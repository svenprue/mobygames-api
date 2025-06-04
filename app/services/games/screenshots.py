from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameScreenshots(BaseScraper):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/game/{self.game_id}/screenshots"

    def get_game_screenshots(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get game name for reference
        game_name = self._get_text(response.xpath("//div[@id='gameTitle']/h1/text()"))

        # Extract screenshots
        screenshot_elements = response.xpath(Games.SCREENSHOTS)
        screenshots = []

        for screenshot in screenshot_elements:
            # Get screenshot URL and caption
            img_url = self._get_text(screenshot.xpath(Games.SCREENSHOT_URL))
            caption = self._get_text(screenshot.xpath(Games.SCREENSHOT_CAPTION))

            # Convert relative URL to absolute if needed
            if img_url and not img_url.startswith('http'):
                img_url = f"{self.base_url}{img_url}"

            # For full-size images, we might need to modify the URL
            # This depends on the actual site structure
            img_url = img_url.replace('/small/', '/large/')

            screenshots.append({
                "url": img_url,
                "caption": caption
            })

        return {
            "game_id": self.game_id,
            "game_name": game_name,
            "screenshots": screenshots
        }

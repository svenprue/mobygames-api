import re
from typing import Dict, List

from app.services.base import BaseScraper
from app.utils.xpath import Critics


class MobyGamesCriticReviews(BaseScraper):
    def __init__(self, critic_id: str, page_number: int = 1):
        super().__init__()
        self.critic_id = critic_id
        self.page_number = page_number
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/critic/{self.critic_id}/reviews?page={self.page_number}"

    def get_critic_reviews(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get critic name for reference
        critic_name = self._get_text(response.xpath(Critics.NAME))

        # Extract reviews section
        reviews_section = response.xpath(Critics.REVIEWS_SECTION)

        # Get review entries
        review_entries = reviews_section.xpath(Critics.REVIEW_ENTRIES)
        reviews = []

        for review_entry in review_entries:
            # Extract game info
            game_title = self._get_text(review_entry.xpath(Critics.GAME_TITLE))
            game_url_path = self._get_text(review_entry.xpath(Critics.GAME_URL))

            # Extract review details
            review_date = self._get_text(review_entry.xpath(Critics.REVIEW_DATE))
            review_score = self._get_text(review_entry.xpath(Critics.REVIEW_SCORE))
            review_text = self._get_text(review_entry.xpath(Critics.REVIEW_TEXT))

            # Extract game ID from URL
            game_id = ""
            if game_url_path:
                match = re.search(r'/game/(\d+)/', game_url_path)
                if match:
                    game_id = match.group(1)

            reviews.append({
                "game_title": game_title,
                "game_url": f"{self.base_url}{game_url_path}" if game_url_path else "",
                "game_id": game_id,
                "date": review_date,
                "score": review_score,
                "text": review_text
            })

        # Get pagination info
        total_pages = 1

        # Look for pagination info in the page
        pagination_text = self._get_text(response.xpath("//div[@class='pagination']/text()"))
        if pagination_text:
            match = re.search(r'of (\d+)', pagination_text)
            if match:
                total_pages = int(match.group(1))

        return {
            "critic_id": self.critic_id,
            "critic_name": critic_name,
            "page_number": self.page_number,
            "total_pages": total_pages,
            "reviews": reviews
        }

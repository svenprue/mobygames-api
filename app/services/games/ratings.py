import re
from typing import Dict, List, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Games


class MobyGamesGameRatings(BaseScraper):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/game/{self.game_id}"

    def get_game_ratings(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get game name for reference
        game_name = self._get_text(response.xpath(Games.TITLE))

        # Extract MobyScore and MobyRank
        moby_score = self._extract_moby_score(response)
        moby_rank = self._extract_moby_rank(response)
        user_rating = self._extract_user_rating(response)
        critic_rating = self._extract_critic_rating(response)

        # Extract age ratings
        age_ratings = self._extract_age_ratings(response)

        # Extract reviews
        reviews = self._extract_reviews(response)

        return {
            "game_id": self.game_id,
            "game_name": game_name,
            "moby_score": moby_score,
            "moby_rank": moby_rank,
            "user_rating": user_rating,
            "critic_rating": critic_rating,
            "age_ratings": age_ratings,
            "reviews": reviews
        }

    def _extract_moby_score(self, response) -> Optional[float]:
        score_text = self._get_text(response.xpath(Games.MOBY_SCORE))
        if score_text:
            try:
                return float(re.search(r'(\d+\.?\d*)', score_text).group(1))
            except (AttributeError, ValueError):
                pass
        return None

    def _extract_moby_rank(self, response) -> Optional[float]:
        rank_text = self._get_text(response.xpath(Games.MOBY_RANK))
        if rank_text:
            try:
                return float(re.search(r'(\d+\.?\d*)', rank_text).group(1))
            except (AttributeError, ValueError):
                pass
        return None

    def _extract_user_rating(self, response) -> Optional[float]:
        rating_text = self._get_text(response.xpath(Games.USER_RATING))
        if rating_text:
            try:
                return float(re.search(r'(\d+\.?\d*)', rating_text).group(1))
            except (AttributeError, ValueError):
                pass
        return None

    def _extract_critic_rating(self, response) -> Optional[float]:
        rating_text = self._get_text(response.xpath(Games.CRITIC_RATING))
        if rating_text:
            try:
                return float(re.search(r'(\d+\.?\d*)', rating_text).group(1))
            except (AttributeError, ValueError):
                pass
        return None

    def _extract_age_ratings(self, response) -> List[Dict]:
        ratings = []

        rating_elements = response.xpath(Games.AGE_RATINGS)
        for element in rating_elements:
            rating_system = self._get_text(element.xpath(Games.RATING_SYSTEM))
            rating = self._get_text(element.xpath(Games.RATING_VALUE))
            descriptors = element.xpath(Games.RATING_DESCRIPTORS)

            if rating_system and rating:
                ratings.append({
                    "rating_system": rating_system,
                    "rating": rating,
                    "content_descriptors": [desc.strip() for desc in descriptors if desc.strip()]
                })

        return ratings

    def _extract_reviews(self, response) -> List[Dict]:
        reviews = []

        review_elements = response.xpath(Games.REVIEWS)
        for element in review_elements:
            reviewer_name = self._get_text(element.xpath(Games.REVIEWER_NAME))
            publication = self._get_text(element.xpath(Games.REVIEW_PUBLICATION))
            score = self._get_text(element.xpath(Games.REVIEW_SCORE))
            max_score = self._get_text(element.xpath(Games.REVIEW_MAX_SCORE))
            review_text = self._get_text(element.xpath(Games.REVIEW_TEXT))
            review_date = self._get_text(element.xpath(Games.REVIEW_DATE))
            review_url = self._get_text(element.xpath(Games.REVIEW_URL))

            if reviewer_name:
                reviews.append({
                    "reviewer_name": reviewer_name,
                    "publication": publication,
                    "score": score,
                    "max_score": max_score,
                    "review_text": review_text,
                    "review_date": review_date,
                    "url": f"{self.base_url}{review_url}" if review_url else None
                })

        return reviews
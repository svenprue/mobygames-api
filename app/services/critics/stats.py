import re
from typing import Dict, List, Optional

from app.services.base import BaseScraper
from app.utils.xpath import Critics


class MobyGamesCriticStats(BaseScraper):
    def __init__(self, critic_id: str):
        super().__init__()
        self.critic_id = critic_id
        self.base_url = "https://www.mobygames.com"

    def _build_url(self) -> str:
        return f"{self.base_url}/critic/{self.critic_id}/stats"

    def get_critic_stats(self) -> Dict:
        url = self._build_url()
        response = self._make_request(url)

        # Get critic name for reference
        critic_name = self._get_text(response.xpath(Critics.NAME))

        # Extract statistics
        total_reviews = self._extract_total_reviews(response)
        average_score = self._extract_average_score(response)
        score_distribution = self._extract_score_distribution(response)
        most_reviewed_genres = self._extract_most_reviewed_genres(response)
        active_years = self._extract_active_years(response)

        return {
            "critic_id": self.critic_id,
            "critic_name": critic_name,
            "total_reviews": total_reviews,
            "average_score": average_score,
            "review_score_distribution": score_distribution,
            "most_reviewed_genres": most_reviewed_genres,
            "active_years": active_years
        }

    def _extract_total_reviews(self, response) -> Optional[int]:
        total_text = self._get_text(response.xpath(Critics.TOTAL_REVIEWS))
        if total_text:
            try:
                return int(re.search(r'(\d+)', total_text).group(1))
            except (AttributeError, ValueError):
                pass
        return None

    def _extract_average_score(self, response) -> Optional[float]:
        avg_text = self._get_text(response.xpath(Critics.AVERAGE_SCORE))
        if avg_text:
            try:
                return float(re.search(r'(\d+\.?\d*)', avg_text).group(1))
            except (AttributeError, ValueError):
                pass
        return None

    def _extract_score_distribution(self, response) -> Optional[dict]:
        distribution = {}

        # Extract score distribution elements
        dist_elements = response.xpath(Critics.SCORE_DISTRIBUTION)

        for element in dist_elements:
            score_range = self._get_text(element.xpath(".//span[@class='range']/text()"))
            count = self._get_text(element.xpath(".//span[@class='count']/text()"))

            if score_range and count:
                try:
                    distribution[score_range] = int(count)
                except ValueError:
                    pass

        return distribution if distribution else None

    def _extract_most_reviewed_genres(self, response) -> Optional[List[str]]:
        genres = []

        genre_elements = response.xpath(Critics.MOST_REVIEWED_GENRES)

        for element in genre_elements:
            genre = element.strip()
            if genre:
                genres.append(genre)

        return genres if genres else None

    def _extract_active_years(self, response) -> Optional[str]:
        return self._get_text(response.xpath(Critics.ACTIVE_YEARS))
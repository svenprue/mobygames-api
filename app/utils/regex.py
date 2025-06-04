# MobyGames URL patterns for extracting IDs and other data

# For extracting game IDs from URLs like "https://www.mobygames.com/game/123/game-name"
REGEX_GAME_ID: str = r"/game/(?P<game_id>\d+)"

# For extracting company IDs from URLs like "https://www.mobygames.com/company/456/company-name"
REGEX_COMPANY_ID: str = r"/company/(?P<company_id>\d+)"

# For extracting person/player IDs from URLs like "https://www.mobygames.com/person/789/person-name"
REGEX_PERSON_ID: str = r"/person/(?P<person_id>\d+)"

# For extracting group IDs from URLs like "https://www.mobygames.com/group/101/group-name"
REGEX_GROUP_ID: str = r"/group/(?P<group_id>\d+)"

# For extracting critic IDs from URLs like "https://www.mobygames.com/critic/202/critic-name"
REGEX_CRITIC_ID: str = r"/critic/(?P<critic_id>\d+)"

# For extracting platform IDs from URLs like "https://www.mobygames.com/platform/303/platform-name"
REGEX_PLATFORM_ID: str = r"/platform/(?P<platform_id>\d+)"

# For parsing years from text like "(1998)" or "Released: 1998"
REGEX_YEAR: str = r"(?P<year>\d{4})"

# For parsing game counts from text like "Involved in 42 games"
REGEX_GAMES_COUNT: str = r"Involved in (?P<count>\d+) games?"

# For parsing review scores from text like "Score: 8.5/10" or "Rating: 4/5"
REGEX_REVIEW_SCORE: str = r"(?P<score>\d+(?:\.\d+)?)\s*/\s*(?P<max_score>\d+)"
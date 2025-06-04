class Games:
    # Updated XPath selectors for actual MobyGames search results table structure
    SEARCH_RESULTS = "//table[@class='table mb']//tr[td]"  # Only get rows with td elements
    GAME_NAME = ".//td[2]//b/a/text()"
    GAME_URL = ".//td[2]//b/a/@href"
    GAME_ID = ".//td[2]//b/a/@href"
    GAME_PLATFORMS_AND_YEAR = ".//td[2]//text() | .//td[2]//small//text()"

    # Alternative selectors for different result layouts
    ALT_SEARCH_RESULTS = "//div[@class='searchResult'] | //table[@class='table mb']//tr"
    ALT_GAME_NAME = ".//div[@class='searchTitle']//a/text() | .//b/a/text()"
    ALT_GAME_URL = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"

    # Game profile
    TITLE = "//div[@id='gameTitle']/h1/text() | //h1/text()"
    PLATFORMS = "//div[@class='platforms']/a/text() | //span[@class='platform']/text()"
    GENRES = "//div[@id='coreGameGenre']//div[@class='innerTab']/text() | //div[@class='genre']/text()"
    DESCRIPTION = "//div[@id='description']/div[@class='desc']/text() | //div[@class='description']/text()"
    RELEASE_INFO = "//div[@class='releaseDate']/text() | //span[@class='release-date']/text()"
    DEVELOPER = "//div[contains(text(), 'Developed by')]/a/text() | //span[@class='developer']/text()"
    PUBLISHER = "//div[contains(text(), 'Published by')]/a/text() | //span[@class='publisher']/text()"

    # Screenshots
    SCREENSHOTS = "//div[@id='screenshotSection']//div[@class='screenshot'] | //div[@class='screenshot']"
    SCREENSHOT_URL = ".//a/img/@src | .//img/@src"
    SCREENSHOT_CAPTION = ".//div[@class='caption']/text() | .//figcaption/text()"

    # Credits
    CREDITS_SECTION = "//div[@id='creditsSection'] | //div[@class='credits']"
    CREDIT_GROUPS = ".//h2/text() | .//h3/text()"
    CREDIT_NAMES = ".//div[@class='role']/text() | .//span[@class='role']/text()"
    CREDIT_PEOPLE = ".//div[@class='credit']/a/text() | .//span[@class='person']/a/text()"
    CREDIT_PEOPLE_URLS = ".//div[@class='credit']/a/@href | .//span[@class='person']/a/@href"

    # Technical Specifications
    TECH_SPECS_REQUIREMENTS = "//div[@class='techSpecs']//div[contains(@class, '{type}')]"
    TECH_SPECS_ATTRIBUTES = "//div[@class='techSpecs']//div[@class='attribute']"
    SPEC_CATEGORY = ".//span[@class='category']/text()"
    SPEC_ATTRIBUTE = ".//span[@class='name']/text()"
    SPEC_VALUE = ".//span[@class='value']/text()"

    # Ratings and Reviews
    MOBY_SCORE = "//div[@class='mobyScore']//span[@class='score']/text() | //span[@class='moby-score']/text()"
    MOBY_RANK = "//div[@class='mobyRank']//span[@class='rank']/text() | //span[@class='moby-rank']/text()"
    USER_RATING = "//div[@class='userRating']//span[@class='rating']/text() | //span[@class='user-rating']/text()"
    CRITIC_RATING = "//div[@class='criticRating']//span[@class='rating']/text() | //span[@class='critic-rating']/text()"

    # Age Ratings
    AGE_RATINGS = "//div[@class='ageRatings']//div[@class='rating'] | //div[@class='age-rating']"
    RATING_SYSTEM = ".//span[@class='system']/text()"
    RATING_VALUE = ".//span[@class='value']/text()"
    RATING_DESCRIPTORS = ".//span[@class='descriptor']/text()"

    # Reviews
    REVIEWS = "//div[@class='reviews']//div[@class='review'] | //div[@class='review-entry']"
    REVIEWER_NAME = ".//span[@class='reviewer']/text() | .//span[@class='reviewer-name']/text()"
    REVIEW_PUBLICATION = ".//span[@class='publication']/text()"
    REVIEW_SCORE = ".//span[@class='score']/text() | .//span[@class='review-score']/text()"
    REVIEW_MAX_SCORE = ".//span[@class='maxScore']/text() | .//span[@class='max-score']/text()"
    REVIEW_TEXT = ".//div[@class='reviewText']/text() | .//div[@class='review-text']/text()"
    REVIEW_DATE = ".//span[@class='date']/text() | .//span[@class='review-date']/text()"
    REVIEW_URL = ".//a[@class='reviewLink']/@href | .//a[@class='review-link']/@href"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text() | //div[@class='trivia-entry']/text()"

    # Releases
    RELEASE_ENTRIES = "//div[@class='releases']//div[@class='release'] | //div[@class='release-entry']"
    RELEASE_PLATFORM = ".//span[@class='platform']/text()"
    RELEASE_REGION = ".//span[@class='region']/text()"
    RELEASE_DATE = ".//span[@class='date']/text() | .//span[@class='release-date']/text()"
    RELEASE_PUBLISHER = ".//span[@class='publisher']/text()"
    RELEASE_DEVELOPER = ".//span[@class='developer']/text()"
    RELEASE_PRODUCT_CODE = ".//span[@class='productCode']/text() | .//span[@class='product-code']/text()"
    RELEASE_AGE_RATING = ".//span[@class='ageRating']/text() | .//span[@class='age-rating']/text()"


class Companies:
    SEARCH_RESULTS = "//div[@class='searchResult'] | //table[@class='table mb']//tr[position()>1]"
    COMPANY_NAME = ".//div[@class='searchTitle']//a/text() | .//b/a/text()"
    COMPANY_URL = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    COMPANY_ID = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    COMPANY_GAMES_COUNT = ".//div[@class='searchDetails']/text() | .//small/text()"

    # Company profile
    NAME = "//div[@id='companyTitle']/h1/text() | //h1/text()"
    OVERVIEW = "//div[@id='companyOverview']/div[@class='desc']/text() | //div[@class='description']/text()"
    FOUNDED = "//div[@id='companyDetails']//div[contains(text(), 'Founded')]/following-sibling::div/text()"
    WEBSITE = "//div[@id='companyDetails']//div[contains(text(), 'Website')]/following-sibling::div/a/@href"
    HEADQUARTERS = "//div[@id='companyDetails']//div[contains(text(), 'Headquarters')]/following-sibling::div/text()"
    STATUS = "//div[@id='companyDetails']//div[contains(text(), 'Status')]/following-sibling::div/text()"
    PARENT_COMPANY = "//div[@id='companyDetails']//div[contains(text(), 'Parent')]/following-sibling::div/a/text()"
    EMPLOYEE_COUNT = "//div[@id='companyDetails']//div[contains(text(), 'Employees')]/following-sibling::div/text()"

    # Company games
    GAMES_SECTION = "//div[@id='companyGames'] | //div[@class='games-section']"
    GAME_ENTRIES = ".//div[@class='gameEntry'] | .//tr"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text() | .//b/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href | .//b/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text() | .//small/text()"
    GAME_YEAR = ".//div[@class='year']/text() | .//span[@class='year']/text()"
    GAME_ROLE = ".//div[@class='role']/text() | .//span[@class='role']/text()"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text() | //div[@class='trivia-entry']/text()"

    # History
    HISTORY_ENTRIES = "//div[@class='history']//div[@class='historyEntry'] | //div[@class='history-entry']"
    HISTORY_DATE = ".//span[@class='date']/text()"
    HISTORY_EVENT = ".//span[@class='event']/text() | .//div[@class='event-text']/text()"


class Developers:
    SEARCH_RESULTS = "//div[@class='searchResult'] | //table[@class='table mb']//tr[position()>1]"
    DEVELOPER_NAME = ".//div[@class='searchTitle']//a/text() | .//b/a/text()"
    DEVELOPER_URL = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    DEVELOPER_ID = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    DEVELOPER_GAMES_COUNT = ".//div[@class='searchDetails']/text() | .//small/text()"

    # Developer profile
    NAME = "//div[@id='developerTitle']/h1/text() | //h1/text()"
    BIO = "//div[@id='developerBio']/div[@class='desc']/text() | //div[@class='bio']/text()"
    KNOWN_ALIASES = "//div[@id='developerAliases']//span[@class='alias']/text() | //span[@class='alias']/text()"
    LOCATION = "//div[@id='developerDetails']//div[contains(text(), 'Location')]/following-sibling::div/text()"
    FOUNDED = "//div[@id='developerDetails']//div[contains(text(), 'Founded')]/following-sibling::div/text()"
    STATUS = "//div[@id='developerDetails']//div[contains(text(), 'Status')]/following-sibling::div/text()"
    TEAM_SIZE = "//div[@id='developerDetails']//div[contains(text(), 'Team')]/following-sibling::div/text()"

    # Developer games
    GAMES_SECTION = "//div[@id='developerGames'] | //div[@class='games-section']"
    GAME_ENTRIES = ".//div[@class='gameEntry'] | .//tr"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text() | .//b/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href | .//b/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text() | .//small/text()"
    GAME_YEAR = ".//div[@class='year']/text() | .//span[@class='year']/text()"
    GAME_ROLE = ".//div[@class='role']/text() | .//span[@class='role']/text()"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text() | //div[@class='trivia-entry']/text()"

    # Tools
    TOOL_ENTRIES = "//div[@class='tools']//div[@class='tool'] | //div[@class='tool-entry']"
    TOOL_NAME = ".//span[@class='name']/text() | .//span[@class='tool-name']/text()"
    TOOL_CATEGORY = ".//span[@class='category']/text() | .//span[@class='tool-category']/text()"


class Groups:
    SEARCH_RESULTS = "//div[@class='searchResult'] | //table[@class='table mb']//tr[position()>1]"
    GROUP_NAME = ".//div[@class='searchTitle']//a/text() | .//b/a/text()"
    GROUP_URL = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    GROUP_ID = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    GROUP_DETAILS = ".//div[@class='searchDetails']/text() | .//small/text()"

    # Group profile
    NAME = "//div[@id='groupTitle']/h1/text() | //h1/text()"
    DESCRIPTION = "//div[@id='groupDescription']/div[@class='desc']/text() | //div[@class='description']/text()"
    MEMBERS = "//div[@id='groupMembers']//div[@class='member'] | //div[@class='member']"
    MEMBER_NAME = ".//a/text()"
    MEMBER_URL = ".//a/@href"
    GROUP_TYPE = "//div[@id='groupDetails']//div[contains(text(), 'Type')]/following-sibling::div/text()"
    FORMED = "//div[@id='groupDetails']//div[contains(text(), 'Formed')]/following-sibling::div/text()"
    STATUS = "//div[@id='groupDetails']//div[contains(text(), 'Status')]/following-sibling::div/text()"

    # Group games
    GAMES_SECTION = "//div[@id='groupGames'] | //div[@class='games-section']"
    GAME_ENTRIES = ".//div[@class='gameEntry'] | .//tr"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text() | .//b/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href | .//b/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text() | .//small/text()"
    GAME_YEAR = ".//div[@class='year']/text() | .//span[@class='year']/text()"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text() | //div[@class='trivia-entry']/text()"


class Critics:
    SEARCH_RESULTS = "//div[@class='searchResult'] | //table[@class='table mb']//tr[position()>1]"
    CRITIC_NAME = ".//div[@class='searchTitle']//a/text() | .//b/a/text()"
    CRITIC_URL = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    CRITIC_ID = ".//div[@class='searchTitle']//a/@href | .//b/a/@href"
    CRITIC_DETAILS = ".//div[@class='searchDetails']/text() | .//small/text()"

    # Critic profile
    NAME = "//div[@id='criticTitle']/h1/text() | //h1/text()"
    BIO = "//div[@id='criticBio']/div[@class='desc']/text() | //div[@class='bio']/text()"
    WEBSITE = "//div[@id='criticDetails']//div[contains(text(), 'Website')]/following-sibling::div/a/@href"
    PUBLICATION = "//div[@id='criticDetails']//div[contains(text(), 'Publication')]/following-sibling::div/text()"
    SPECIALIZATION = "//div[@id='criticDetails']//div[contains(text(), 'Specialization')]/following-sibling::div/span/text()"

    # Critic reviews
    REVIEWS_SECTION = "//div[@id='criticReviews'] | //div[@class='reviews-section']"
    REVIEW_ENTRIES = ".//div[@class='reviewEntry'] | .//div[@class='review-entry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text() | .//b/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href | .//b/a/@href"
    REVIEW_DATE = ".//div[@class='reviewDate']/text() | .//span[@class='date']/text()"
    REVIEW_SCORE = ".//div[@class='reviewScore']/text() | .//span[@class='score']/text()"
    REVIEW_TEXT = ".//div[@class='reviewText']/text() | .//div[@class='review-text']/text()"

    # Critic stats
    TOTAL_REVIEWS = "//div[@class='stats']//span[@class='totalReviews']/text() | //span[@class='total-reviews']/text()"
    AVERAGE_SCORE = "//div[@class='stats']//span[@class='averageScore']/text() | //span[@class='average-score']/text()"
    SCORE_DISTRIBUTION = "//div[@class='stats']//div[@class='scoreDistribution'] | //div[@class='score-distribution']"
    MOST_REVIEWED_GENRES = "//div[@class='stats']//div[@class='genres']/span/text() | //span[@class='genre']/text()"
    ACTIVE_YEARS = "//div[@class='stats']//span[@class='activeYears']/text() | //span[@class='active-years']/text()"


class Pagination:
    PAGE_NUMBER_LAST = "//li[contains(@class, 'list-item--icon-last-page')]//@href | //a[@class='last']/@href"
    PAGE_NUMBER_ACTIVE = "//li[contains(@class, 'list-item--active')]//@href | //a[@class='active']/@href"
    PAGINATION_INFO = "//div[@class='pagination']//text() | //nav[@class='pagination']//text()"
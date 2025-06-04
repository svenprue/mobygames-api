class Games:
    SEARCH_RESULTS = "//div[@class='searchResult']"
    GAME_NAME = ".//div[@class='searchTitle']//a/text()"
    GAME_URL = ".//div[@class='searchTitle']//a/@href"
    GAME_ID = ".//div[@class='searchTitle']//a/@href"
    GAME_PLATFORMS = ".//div[@class='searchDetails']/span[@class='platform']/text()"
    GAME_YEAR = ".//div[@class='searchDetails']/span[@class='platform']/following-sibling::text()"

    # Game profile
    TITLE = "//div[@id='gameTitle']/h1/text()"
    PLATFORMS = "//div[@class='platforms']/a/text()"
    GENRES = "//div[@id='coreGameGenre']//div[@class='innerTab']/text()"
    DESCRIPTION = "//div[@id='description']/div[@class='desc']/text()"
    RELEASE_INFO = "//div[@class='releaseDate']/text()"
    DEVELOPER = "//div[contains(text(), 'Developed by')]/a/text()"
    PUBLISHER = "//div[contains(text(), 'Published by')]/a/text()"

    # Screenshots
    SCREENSHOTS = "//div[@id='screenshotSection']//div[@class='screenshot']"
    SCREENSHOT_URL = ".//a/img/@src"
    SCREENSHOT_CAPTION = ".//div[@class='caption']/text()"

    # Credits
    CREDITS_SECTION = "//div[@id='creditsSection']"
    CREDIT_GROUPS = ".//h2/text()"
    CREDIT_NAMES = ".//div[@class='role']/text()"
    CREDIT_PEOPLE = ".//div[@class='credit']/a/text()"
    CREDIT_PEOPLE_URLS = ".//div[@class='credit']/a/@href"

    # Technical Specifications
    TECH_SPECS_REQUIREMENTS = "//div[@class='techSpecs']//div[contains(@class, '{type}')]"
    TECH_SPECS_ATTRIBUTES = "//div[@class='techSpecs']//div[@class='attribute']"
    SPEC_CATEGORY = ".//span[@class='category']/text()"
    SPEC_ATTRIBUTE = ".//span[@class='name']/text()"
    SPEC_VALUE = ".//span[@class='value']/text()"

    # Ratings and Reviews
    MOBY_SCORE = "//div[@class='mobyScore']//span[@class='score']/text()"
    MOBY_RANK = "//div[@class='mobyRank']//span[@class='rank']/text()"
    USER_RATING = "//div[@class='userRating']//span[@class='rating']/text()"
    CRITIC_RATING = "//div[@class='criticRating']//span[@class='rating']/text()"

    # Age Ratings
    AGE_RATINGS = "//div[@class='ageRatings']//div[@class='rating']"
    RATING_SYSTEM = ".//span[@class='system']/text()"
    RATING_VALUE = ".//span[@class='value']/text()"
    RATING_DESCRIPTORS = ".//span[@class='descriptor']/text()"

    # Reviews
    REVIEWS = "//div[@class='reviews']//div[@class='review']"
    REVIEWER_NAME = ".//span[@class='reviewer']/text()"
    REVIEW_PUBLICATION = ".//span[@class='publication']/text()"
    REVIEW_SCORE = ".//span[@class='score']/text()"
    REVIEW_MAX_SCORE = ".//span[@class='maxScore']/text()"
    REVIEW_TEXT = ".//div[@class='reviewText']/text()"
    REVIEW_DATE = ".//span[@class='date']/text()"
    REVIEW_URL = ".//a[@class='reviewLink']/@href"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text()"

    # Releases
    RELEASE_ENTRIES = "//div[@class='releases']//div[@class='release']"
    RELEASE_PLATFORM = ".//span[@class='platform']/text()"
    RELEASE_REGION = ".//span[@class='region']/text()"
    RELEASE_DATE = ".//span[@class='date']/text()"
    RELEASE_PUBLISHER = ".//span[@class='publisher']/text()"
    RELEASE_DEVELOPER = ".//span[@class='developer']/text()"
    RELEASE_PRODUCT_CODE = ".//span[@class='productCode']/text()"
    RELEASE_AGE_RATING = ".//span[@class='ageRating']/text()"


class Companies:
    SEARCH_RESULTS = "//div[@class='searchResult']"
    COMPANY_NAME = ".//div[@class='searchTitle']//a/text()"
    COMPANY_URL = ".//div[@class='searchTitle']//a/@href"
    COMPANY_ID = ".//div[@class='searchTitle']//a/@href"
    COMPANY_GAMES_COUNT = ".//div[@class='searchDetails']/text()"

    # Company profile
    NAME = "//div[@id='companyTitle']/h1/text()"
    OVERVIEW = "//div[@id='companyOverview']/div[@class='desc']/text()"
    FOUNDED = "//div[@id='companyDetails']//div[contains(text(), 'Founded')]/following-sibling::div/text()"
    WEBSITE = "//div[@id='companyDetails']//div[contains(text(), 'Website')]/following-sibling::div/a/@href"
    HEADQUARTERS = "//div[@id='companyDetails']//div[contains(text(), 'Headquarters')]/following-sibling::div/text()"
    STATUS = "//div[@id='companyDetails']//div[contains(text(), 'Status')]/following-sibling::div/text()"
    PARENT_COMPANY = "//div[@id='companyDetails']//div[contains(text(), 'Parent')]/following-sibling::div/a/text()"
    EMPLOYEE_COUNT = "//div[@id='companyDetails']//div[contains(text(), 'Employees')]/following-sibling::div/text()"

    # Company games
    GAMES_SECTION = "//div[@id='companyGames']"
    GAME_ENTRIES = ".//div[@class='gameEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text()"
    GAME_YEAR = ".//div[@class='year']/text()"
    GAME_ROLE = ".//div[@class='role']/text()"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text()"

    # History
    HISTORY_ENTRIES = "//div[@class='history']//div[@class='historyEntry']"
    HISTORY_DATE = ".//span[@class='date']/text()"
    HISTORY_EVENT = ".//span[@class='event']/text()"


class Developers:
    SEARCH_RESULTS = "//div[@class='searchResult']"
    DEVELOPER_NAME = ".//div[@class='searchTitle']//a/text()"
    DEVELOPER_URL = ".//div[@class='searchTitle']//a/@href"
    DEVELOPER_ID = ".//div[@class='searchTitle']//a/@href"
    DEVELOPER_GAMES_COUNT = ".//div[@class='searchDetails']/text()"

    # Developer profile
    NAME = "//div[@id='developerTitle']/h1/text()"
    BIO = "//div[@id='developerBio']/div[@class='desc']/text()"
    KNOWN_ALIASES = "//div[@id='developerAliases']//span[@class='alias']/text()"
    LOCATION = "//div[@id='developerDetails']//div[contains(text(), 'Location')]/following-sibling::div/text()"
    FOUNDED = "//div[@id='developerDetails']//div[contains(text(), 'Founded')]/following-sibling::div/text()"
    STATUS = "//div[@id='developerDetails']//div[contains(text(), 'Status')]/following-sibling::div/text()"
    TEAM_SIZE = "//div[@id='developerDetails']//div[contains(text(), 'Team')]/following-sibling::div/text()"

    # Developer games
    GAMES_SECTION = "//div[@id='developerGames']"
    GAME_ENTRIES = ".//div[@class='gameEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text()"
    GAME_YEAR = ".//div[@class='year']/text()"
    GAME_ROLE = ".//div[@class='role']/text()"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text()"

    # Tools
    TOOL_ENTRIES = "//div[@class='tools']//div[@class='tool']"
    TOOL_NAME = ".//span[@class='name']/text()"
    TOOL_CATEGORY = ".//span[@class='category']/text()"


class Groups:
    SEARCH_RESULTS = "//div[@class='searchResult']"
    GROUP_NAME = ".//div[@class='searchTitle']//a/text()"
    GROUP_URL = ".//div[@class='searchTitle']//a/@href"
    GROUP_ID = ".//div[@class='searchTitle']//a/@href"
    GROUP_DETAILS = ".//div[@class='searchDetails']/text()"

    # Group profile
    NAME = "//div[@id='groupTitle']/h1/text()"
    DESCRIPTION = "//div[@id='groupDescription']/div[@class='desc']/text()"
    MEMBERS = "//div[@id='groupMembers']//div[@class='member']"
    MEMBER_NAME = ".//a/text()"
    MEMBER_URL = ".//a/@href"
    GROUP_TYPE = "//div[@id='groupDetails']//div[contains(text(), 'Type')]/following-sibling::div/text()"
    FORMED = "//div[@id='groupDetails']//div[contains(text(), 'Formed')]/following-sibling::div/text()"
    STATUS = "//div[@id='groupDetails']//div[contains(text(), 'Status')]/following-sibling::div/text()"

    # Group games
    GAMES_SECTION = "//div[@id='groupGames']"
    GAME_ENTRIES = ".//div[@class='gameEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text()"
    GAME_YEAR = ".//div[@class='year']/text()"

    # Trivia
    TRIVIA_ENTRIES = "//div[@class='trivia']//div[@class='triviaEntry']/text()"


class Critics:
    SEARCH_RESULTS = "//div[@class='searchResult']"
    CRITIC_NAME = ".//div[@class='searchTitle']//a/text()"
    CRITIC_URL = ".//div[@class='searchTitle']//a/@href"
    CRITIC_ID = ".//div[@class='searchTitle']//a/@href"
    CRITIC_DETAILS = ".//div[@class='searchDetails']/text()"

    # Critic profile
    NAME = "//div[@id='criticTitle']/h1/text()"
    BIO = "//div[@id='criticBio']/div[@class='desc']/text()"
    WEBSITE = "//div[@id='criticDetails']//div[contains(text(), 'Website')]/following-sibling::div/a/@href"
    PUBLICATION = "//div[@id='criticDetails']//div[contains(text(), 'Publication')]/following-sibling::div/text()"
    SPECIALIZATION = "//div[@id='criticDetails']//div[contains(text(), 'Specialization')]/following-sibling::div/span/text()"

    # Critic reviews
    REVIEWS_SECTION = "//div[@id='criticReviews']"
    REVIEW_ENTRIES = ".//div[@class='reviewEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    REVIEW_DATE = ".//div[@class='reviewDate']/text()"
    REVIEW_SCORE = ".//div[@class='reviewScore']/text()"
    REVIEW_TEXT = ".//div[@class='reviewText']/text()"

    # Critic stats
    TOTAL_REVIEWS = "//div[@class='stats']//span[@class='totalReviews']/text()"
    AVERAGE_SCORE = "//div[@class='stats']//span[@class='averageScore']/text()"
    SCORE_DISTRIBUTION = "//div[@class='stats']//div[@class='scoreDistribution']"
    MOST_REVIEWED_GENRES = "//div[@class='stats']//div[@class='genres']/span/text()"
    ACTIVE_YEARS = "//div[@class='stats']//span[@class='activeYears']/text()"


class Pagination:
    PAGE_NUMBER_LAST = "//li[contains(@class, 'list-item--icon-last-page')]//@href"
    PAGE_NUMBER_ACTIVE = "//li[contains(@class, 'list-item--active')]//@href"
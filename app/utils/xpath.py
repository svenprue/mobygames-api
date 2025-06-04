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

    # Company games
    GAMES_SECTION = "//div[@id='companyGames']"
    GAME_ENTRIES = ".//div[@class='gameEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text()"
    GAME_YEAR = ".//div[@class='year']/text()"
    GAME_ROLE = ".//div[@class='role']/text()"

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

    # Developer games
    GAMES_SECTION = "//div[@id='developerGames']"
    GAME_ENTRIES = ".//div[@class='gameEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text()"
    GAME_YEAR = ".//div[@class='year']/text()"
    GAME_ROLE = ".//div[@class='role']/text()"

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

    # Group games
    GAMES_SECTION = "//div[@id='groupGames']"
    GAME_ENTRIES = ".//div[@class='gameEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    GAME_PLATFORMS = ".//div[@class='platforms']/span/text()"
    GAME_YEAR = ".//div[@class='year']/text()"

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

    # Critic reviews
    REVIEWS_SECTION = "//div[@id='criticReviews']"
    REVIEW_ENTRIES = ".//div[@class='reviewEntry']"
    GAME_TITLE = ".//div[@class='gameTitle']/a/text()"
    GAME_URL = ".//div[@class='gameTitle']/a/@href"
    REVIEW_DATE = ".//div[@class='reviewDate']/text()"
    REVIEW_SCORE = ".//div[@class='reviewScore']/text()"
    REVIEW_TEXT = ".//div[@class='reviewText']/text()"

class Pagination:
    PAGE_NUMBER_LAST = "//li[contains(@class, 'list-item--icon-last-page')]//@href"
    PAGE_NUMBER_ACTIVE = "//li[contains(@class, 'list-item--active')]//@href"
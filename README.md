# transfermarkt-api

This project provides a lightweight and easy-to-use interface for extracting data from [Transfermarkt](https://www.transfermarkt.com/) 
by applying web scraping processes and offering a RESTful API service via FastAPI. With this service, developers can 
seamlessly integrate Transfermarkt data into their applications, websites, or data analysis pipelines.

Please note that the deployed application is used only for testing purposes and has a rate limiting 
feature enabled. If you'd like to customize it, consider hosting in your own cloud service. 

### API Swagger
https://transfermarkt-api.fly.dev/

### Running Locally

````bash
# Clone the repository
$ git clone https://github.com/felipeall/transfermarkt-api.git

# Go to the project's root folder
$ cd transfermarkt-api

# Activate Python environment
$ python -m venv .venv
$ .venv\Scripts\activate  # On Windows
# $ source .venv/bin/activate  # On Unix/macOS

# Set up Poetry environment
$ poetry env use python
$ poetry install --no-root

# Start the API server
$ poetry run uvicorn app.main:app --reload
# MobyGames API Scraper

A FastAPI-based scraper for retrieving data from MobyGames.com, focused on providing structured access to information about games, players (people), companies, groups, and critics.

## Features

### Games
- Search games by name
- Get detailed game profiles
- Retrieve game screenshots
- Access game credits

### Players
- Search people by name
- Get player profiles
- View player credits (games worked on)

### Companies
- Search companies by name
- Get company profiles
- View games associated with companies

### Groups
- Search groups by name
- Get group profiles
- View games associated with groups

### Critics
- Search critics by name
- Get critic profiles
- View reviews written by critics

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd <repository-directory>

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Start the FastAPI server
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

Access the interactive API documentation at http://localhost:8000/docs

## API Endpoints

### Games
- GET `/games/search/{game_name}` - Search for games by name
- GET `/games/{game_id}/profile` - Get detailed game information
- GET `/games/{game_id}/screenshots` - Get game screenshots
- GET `/games/{game_id}/credits` - Get game credits

### Players
- GET `/players/search/{player_name}` - Search for players by name
- GET `/players/{player_id}/profile` - Get player profile
- GET `/players/{player_id}/credits` - Get player credits

### Companies
- GET `/companies/search/{company_name}` - Search for companies by name
- GET `/companies/{company_id}/profile` - Get company profile
- GET `/companies/{company_id}/games` - Get games associated with company

### Groups
- GET `/groups/search/{group_name}` - Search for groups by name
- GET `/groups/{group_id}/profile` - Get group profile
- GET `/groups/{group_id}/games` - Get games associated with group

### Critics
- GET `/critics/search/{critic_name}` - Search for critics by name
- GET `/critics/{critic_id}/profile` - Get critic profile
- GET `/critics/{critic_id}/reviews` - Get reviews by critic

## Disclaimer

This project is for educational purposes only. Please respect MobyGames' terms of service and robots.txt when using this scraper. Consider adding appropriate rate limiting and caching to avoid overwhelming their servers.
# Access the API local page
$ open http://localhost:8000/  # On macOS
# Or navigate to http://localhost:8000/ in your browser
````

### Running via Docker

````bash
# Clone the repository
$ git clone https://github.com/felipeall/transfermarkt-api.git

# Go to the project's root folder
$ cd transfermarkt-api

# Build the Docker image
$ docker build -t transfermarkt-api . 

# Instantiate the Docker container
$ docker run -d -p 8000:8000 transfermarkt-api

# Access the API local page
$ open http://localhost:8000/
````

### Environment Variables

| Variable                  | Description                                               | Default      |
|---------------------------|-----------------------------------------------------------|--------------|
| `RATE_LIMITING_ENABLE`    | Enable rate limiting feature for API calls                | `false`      |
| `RATE_LIMITING_FREQUENCY` | Delay allowed between each API call. See [slowapi](https://slowapi.readthedocs.io/en/latest/) for more | `2/3seconds` |

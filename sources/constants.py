__author__ = "MAK"

import os

NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
CACHE_EXPIRY_TIME = 60  # seconds
API_CONSUMPTION_TIMELIMIT = 6  # seconds

REDDIT_CONFIG = {
    "general": {
        "url": "https://www.reddit.com/r/news/.json",
        "headers": {"User-agent": "Meddy Kasem bot 0.1"},
    },
    "search": {
        "url": "https://www.reddit.com/r/news/search.json",
        "headers": {"User-agent": "Meddy Kasem bot 0.1"},
    },
}

NEWSAPI_CONFIG = {
    "general": {
        "url": "https://newsapi.org/v2/top-headlines",
        "headers": {"Authorization": NEWSAPI_KEY},
        "payload": {"category": "general", "language": "en"},
    },
    "search": {
        "url": "https://newsapi.org/v2/everything",
        "headers": {"Authorization": NEWSAPI_KEY},
        "payload": {"language": "en", "sortBy": "relevance"},
    },
}

### ADD Additional API configs here

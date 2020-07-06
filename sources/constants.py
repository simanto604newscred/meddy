__author__ = "MAK"

import os


NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY", "4afff5e8732e41f5861dbf8899503738")
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


MEDDY_API_CONFIG = {
    "general": {
        "url": "http://628dc6d9095c.ngrok.io/news/",
        "method": "POST",
        "headers": {},
    },
    "search": {
        "url": "http://628dc6d9095c.ngrok.io/news/search",
        "method": "POST",
        "headers": {},
    },
    "get_key": {
        "url": "http://628dc6d9095c.ngrok.io/key",
        "method": "GET",
        "headers": {},
    },
}
### ADD Additional API configs here

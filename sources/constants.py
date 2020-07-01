__author__ = "MAK"

import os

NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")

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

top_headlines_url = "https://newsapi.org/v2/top-headlines"
# To fetch news articles
everything_news_url = "https://newsapi.org/v2/everything"
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

CACHE_EXPIRY_TIME = 60  # seconds

__author__ = "MAK"


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
        "headers": {"Authorization": "4afff5e8732e41f5861dbf8899503738"},
        "payload": {"category": "general", "language": "en"}
    },
    "search": {
        "url": "https://newsapi.org/v2/everything",
        "headers": {"Authorization": "4afff5e8732e41f5861dbf8899503738"},
        "payload": {"language": "en", "sortBy": "relevance"}
    },
}
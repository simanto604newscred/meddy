__author__ = "MAK"

from sources.reddit import RedditFactory
from sources.news_api import NewsAPIFactory


SOURCE_MAP = {
    # "newsapi" : NewsAPIFactory,
    "reddit": RedditFactory,
}

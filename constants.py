__author__ = "MAK"

from sources.news_api import NewsAPIFactory
from sources.reddit import RedditFactory

SOURCE_MAP = {
    "newsapi": NewsAPIFactory,
    "reddit": RedditFactory,
    # add new factory for additional API
}

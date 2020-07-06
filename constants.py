__author__ = "MAK"

from sources.news_api import NewsAPIFactory
from sources.reddit import RedditFactory
from sources.meddy import MeddyFactory

SOURCE_MAP = {
    "newsapi": NewsAPIFactory,
    "reddit": RedditFactory,
    "meddy": MeddyFactory,
    # add new factory for additional API
}

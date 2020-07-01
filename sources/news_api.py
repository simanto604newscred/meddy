__author__ = "MAK"
from pydantic.dataclasses import dataclass

from .constants import NEWSAPI_CONFIG
from .source_base import SourceBase, FactoryBase


@dataclass
class NewsAPI(SourceBase):
    def prepare_payload(self, query):
        self.payload.update({"q": query})

    def prepare_source_specific_response(self, response):
        data = [
            {"headline": i.get("title"), "link": i.get("url"), "source": "newsapi",}
            for i in response.json().get("articles", [])
        ]
        return data


@dataclass
class NewsAPIFactory(FactoryBase):
    def make_source_object(self):
        if self.search_enabled:
            return NewsAPI(**(NEWSAPI_CONFIG.get("search")))

        return NewsAPI(**(NEWSAPI_CONFIG.get("general")))

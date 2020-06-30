__author__ = "MAK"
from pydantic.dataclasses import dataclass
from .source_base import SourceBase, FactoryBase
from .constants import REDDIT_CONFIG


@dataclass
class Reddit(SourceBase):
    def prepare_source_specific_response(self, response):
        data = [
            {
                "headline": i.get("data", {}).get("title"),
                "link": i.get("data", {}).get("url"),
                "source": "reddit",
            }
            for i in response.json().get("data", {}).get("children", [])
        ]
        return data

    def prepare_payload(self, query):
        self.payload = {"q": query}


@dataclass
class RedditFactory(FactoryBase):
    def make_source_object(self):
        if self.search_enabled:
            return Reddit(**(REDDIT_CONFIG.get("search")))

        return Reddit(**(REDDIT_CONFIG.get("general")))

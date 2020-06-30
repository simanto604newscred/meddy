__author__ = "MAK"
from pydantic.dataclasses import dataclass

from .source_base import SourceBase, FactoryBase


@dataclass
class NewsAPI(SourceBase):
    pass


@dataclass
class NewsAPIFactory(FactoryBase):
    def make_source_object(self):
        return

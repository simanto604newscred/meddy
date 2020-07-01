import json
from dataclasses import field

from pydantic.dataclasses import dataclass

from .utils import get_or_create_cached_response


@dataclass
class SourceBase:
    headers: dict
    url: str
    payload: dict = field(default_factory=dict)

    def prepare_headers(self):
        raise NotImplementedError()

    def prepare_payload(self, *args, **kwargs):
        raise NotImplementedError()

    def get_response(self):
        params = json.dumps({"cache_key": [self.url, self.headers, self.payload]})
        return get_or_create_cached_response(params=params)

    def prepare_source_specific_response(self, response):
        raise NotImplementedError()


@dataclass
class FactoryBase:
    search_enabled: bool = False

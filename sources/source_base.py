from pydantic.dataclasses import dataclass
from dataclasses import field
import requests


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
        response = requests.get(url=self.url, headers=self.headers, params=self.payload)
        return response

    def prepare_source_specific_response(self, response):
        raise NotImplementedError()


@dataclass
class FactoryBase:
    search_enabled: bool = False

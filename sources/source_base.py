import json
from dataclasses import field

from pydantic.dataclasses import dataclass

from .utils import get_or_create_cached_response


@dataclass
class SourceBase:
    """
    Any new source added will inherit this base class
    """

    headers: dict
    url: str
    payload: dict = field(default_factory=dict)

    def prepare_headers(self):
        """
        prepare headers if necessary by implementing in concreate source child class
        :return:
        """
        pass

    def prepare_payload(self, query, *args, **kwargs):
        """
        Must implement in concrete source child class to add additional payloads for search
        :argument query: user defined parameter is relayed using this
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    def get_response(self):
        params = json.dumps(
            {"cache_key": [self.url, self.headers, self.payload]}
        )  # make hashable for caching
        return get_or_create_cached_response(params=params)

    def prepare_source_specific_response(self, response):
        """
        Must implement in concrete source child class to format/parse from raw response
        :return:
        """
        raise NotImplementedError()


@dataclass
class FactoryBase:
    """
    Any new source factory added will inherit this base factory
    """

    search_enabled: bool = False

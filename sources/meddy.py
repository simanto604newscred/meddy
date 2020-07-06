import logging

import requests
from pydantic.dataclasses import dataclass
from requests.exceptions import (
    ConnectTimeout,
    HTTPError,
    ReadTimeout,
    Timeout,
    ConnectionError,
)

from .constants import MEDDY_API_CONFIG, API_CONSUMPTION_TIMELIMIT
from .source_base import SourceBase, FactoryBase

logger = logging.getLogger(__name__)


@dataclass
class Meddy(SourceBase):
    @staticmethod
    def get_key():
        try:
            method = MEDDY_API_CONFIG.get("get_key").get("method")
            url = MEDDY_API_CONFIG.get("get_key", {}).get("url")
            response = requests.request(
                method=method, url=url, timeout=API_CONSUMPTION_TIMELIMIT
            )
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
            logger.exception(f"Exception Occurred. returning False as response")
            return False

        return response.json()

    def prepare_headers(self):

        self.payload = self.get_key() if self.get_key() else None

    def prepare_source_specific_response(self, response):

        return response

    def prepare_payload(self, query):
        self.payload.update({"query": query})


@dataclass
class MeddyFactory(FactoryBase):
    def make_source_object(self):
        if self.search_enabled:
            return Meddy(**(MEDDY_API_CONFIG.get("search")))

        return Meddy(**(MEDDY_API_CONFIG.get("general")))

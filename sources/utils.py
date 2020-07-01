import json
import logging

import requests
from cachetools import cached, TTLCache
from requests.exceptions import (
    ConnectTimeout,
    HTTPError,
    ReadTimeout,
    Timeout,
    ConnectionError,
)

from .constants import CACHE_EXPIRY_TIME, API_CONSUMPTION_TIMELIMIT

logger = logging.getLogger(__name__)


@cached(
    cache=TTLCache(maxsize=1024, ttl=CACHE_EXPIRY_TIME)
)  # TODO replace this with distributed key_value cache like REDIS
def get_or_create_cached_response(params):
    url, headers, payload = json.loads(params).get("cache_key")
    try:
        response = requests.get(
            url=url, headers=headers, params=payload, timeout=API_CONSUMPTION_TIMELIMIT
        )  # Todo change this to async request client aiohttp
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
        logger.exception(f"Exception Occurred. returning False as response")
        return False

    return response.json()

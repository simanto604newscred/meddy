import requests
from cachetools import cached, TTLCache
import json
from .constants import CACHE_EXPIRY_TIME


@cached(
    cache=TTLCache(maxsize=1024, ttl=CACHE_EXPIRY_TIME)
)  # TODO replace this with distributed key_value cache like REDIS
def get_or_create_cached_response(params):
    url, headers, payload = json.loads(params).get("cache_key")
    response = requests.get(url=url, headers=headers, params=payload)
    return response

import json
import os

from constants import SOURCE_MAP
from sources.news_api import NewsAPI
from sources.reddit import Reddit
from sources.utils import requests


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200


def test_news(client, mocker):
    mocker.patch.object(requests, "get")
    spy = mocker.spy(requests, "get")
    requests.get.return_value.status = 200
    requests.get.return_value.json.return_value = {}
    response = client.get("/news")
    assert response.status_code == 200
    assert response.json() == []
    assert spy.call_count == len(SOURCE_MAP)


def test_get_or_create_cached_response(client, mocker):
    mocker.patch.object(requests, "get")
    spy = mocker.spy(requests, "get")
    response = client.get("/news?query=bitcoin")  # create cache_entry
    assert spy.call_count == len(SOURCE_MAP)
    response = client.get("/news?query=bitcoin")  # retrieve cache_entry
    assert spy.call_count == len(
        SOURCE_MAP
    )  # as retrieved from, cache call count doesn't increase
    response = client.get("/news?query=coin")
    assert spy.call_count == len(SOURCE_MAP) * 2
    response = client.get("/news?query=bit")
    assert spy.call_count == len(SOURCE_MAP) * 3


def test_redit_prepare_source_specific_response():
    FILE_NAME = "reddit_sample.json"
    DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), FILE_NAME)
    with open(DATA_FILE_PATH) as f:
        data = json.load(f)
    response_json = data
    expected = [
        {
            "headline": "2 teenagers charged with murder in alleyway beating death of 63-year-old homeless man",
            "link": "https://abcnews.go.com/US/teenagers-charged-murder-alleyway-beating-death-63-year/story?id=71550327",
            "source": "reddit",
        }
    ]

    reddit = Reddit(headers={}, url="fake")
    actual = reddit.prepare_source_specific_response(response_json)

    assert actual == expected


def test_newsapi_prepare_source_specific_response():

    response_json = json.loads(
        """
    {"status": "ok", "totalResults": 1854, "articles": [{"source": {"id": null, "name": "Daily Mail"},
     "author": "By Sam Blanchard Senior Health Reporter For Mailonli",
     "title": "Flooded Bitcoin mining farm",
     "description": "The areas most at risk of local lockdowns like ",
     "url": "https://imgur.com/2R7KIbF",
     "urlToImage": "https://i.dailymail.co.uk/1s/2020/07/01/15/30274042-0-image-a-18_1593615027021.jpg",
     "publishedAt": "2020-07-01T16:46:36Z",
     "content": "Bradford, Barnsley and Rochdale are three of the areas"}]}
                                                         """
    )
    expected = [
        {
            "headline": "Flooded Bitcoin mining farm",
            "link": "https://imgur.com/2R7KIbF",
            "source": "newsapi",
        }
    ]

    newsapi = NewsAPI(headers={}, url="fake")
    actual = newsapi.prepare_source_specific_response(response_json)

    assert actual == expected

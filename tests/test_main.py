from constants import SOURCE_MAP
from sources.utils import requests


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

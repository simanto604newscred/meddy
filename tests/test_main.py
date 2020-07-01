from sources.source_base import requests
from constants import SOURCE_MAP


def test_news(client, mocker):
    mocker.patch.object(requests, 'get')
    spy = mocker.spy(requests, 'get')
    requests.get.return_value.status = 200
    requests.get.return_value.json.return_value = {}
    response = client.get("/news")
    assert response.status_code == 200
    assert response.json() == []
    assert spy.call_count == len(SOURCE_MAP)



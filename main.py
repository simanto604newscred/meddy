import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/news")
def news(query: str = None):
    from aggregator import aggregate_all

    data = aggregate_all(search_query=query)
    return data


@app.get("/")
def read_root():
    import requests
    import json
    headers = {"Authorization": "4afff5e8732e41f5861dbf8899503738"}

    top_headlines_url = "https://newsapi.org/v2/top-headlines"
    # To fetch news articles
    everything_news_url = "https://newsapi.org/v2/everything"
    # To retrieve the sources
    sources_url = "https://newsapi.org/v2/sources"

    # Add parameters to request URL based on what type of headlines news you want

    # All the payloads in this section
    # headlines_payload = {'category': 'business', 'country': 'us'}
    everything_payload = {"q": "finance", "language": "en", "sortBy": "popularity"}
    # sources_payload = {'category': 'general', 'language': 'en', 'country': 'us'}

    # Fire a request based on the requirement, just change the url and the params field

    # Request to fetch the top headlines
    # response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)

    # Request to fetch every news article
    response = requests.get(
        url=everything_news_url, headers=headers, params=everything_payload
    )

    # Request to fetch the sources
    # response = requests.get(url=sources_url, headers=headers, params=sources_payload)

    # If you just want to print
    pretty_json_output = json.dumps(response.json(), indent=4)
    print(pretty_json_output)
    # print(response.json())

    # To store the relevant json data to a csv

    # Convert response to a pure json string
    response_json_string = json.dumps(response.json())

    # A json object is equivalent to a dictionary in Python
    # retrieve json objects to a python dict
    response_dict = json.loads(response_json_string)
    print(response_dict)

    articles_list = response_dict["articles"]

    return articles_list


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

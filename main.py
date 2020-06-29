import json

import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/reddit")
def reddit():
    everything_news_url = "https://www.reddit.com/r/news/search.json"
    everything_payload = {"q": "bitcoin"}
    headers = {"User-agent": "Meddy Kasem bot 0.1"}
    response = requests.get(
        url=everything_news_url, headers=headers, params=everything_payload
    )

    data = [
        {
            "headline": i.get("data", {}).get("title"),
            "link": i.get("data", {}).get("url"),
        }
        for i in response.json().get("data", {}).get("children", [])
    ]

    return data



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

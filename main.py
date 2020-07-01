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
    return {"Hello": "I am alive"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

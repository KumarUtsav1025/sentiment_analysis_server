from typing import Union
import sentiment_analyser as sa
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    positive, negative, neutral = sa.get_sentiment()
    return {"positive": positive, "negative": negative, "neutral": neutral}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
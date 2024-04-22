import requests
from fastapi import FastAPI
from auth import Auth
from joke import Joke
from logging_middleware import LoggingMiddleware

app = FastAPI()


@app.get("/joke")
async def root():
    response = requests.get("https://api.chucknorris.io/jokes/random").json()
    Joke.from_dict(response)
    return Joke.from_dict(response)


app.add_middleware(Auth)
app.add_middleware(LoggingMiddleware)

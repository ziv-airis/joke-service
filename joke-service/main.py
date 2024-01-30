import requests
from fastapi import FastAPI
from auth import Auth
from ofeklogger.log import Log

from joke import Joke
app = FastAPI()

@app.get("/joke")
async def root():
    response = requests.get("https://api.chucknorris.io/jokes/random").json()
    Joke.from_dict(response)
    return Joke.from_dict(response)

# The last add_middleware will be called first
app.add_middleware(Auth) # The order matters, this way the Auth will be seccond (because in UNAUTHORIZED situations will return immidiatly and I want to write the log)
app.add_middleware(Log)

from typing import Union

from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000 this is my api endpoint
@app.get("/")
def read_root():
    return {"Description": "Celtics will be the championship this season"}

# get another function
@app.get("/jasontatum")
def read_root():
    return {"Description": "The personal stat of Jason Tatum in the game with Piston", "Points": 43, "Rebound": 10, "Assist": 3}



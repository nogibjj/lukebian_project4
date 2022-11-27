import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum


class Players(BaseModel):
    name: str
    position: str
    college: str
    shoots: str
app = FastAPI()

Players_FILE = "players.json"
PLAYERS = []

if os.path.exists(Players_FILE):
    with open(Players_FILE, "r") as f:
        PLAYERS = json.load(f)


# http://127.0.0.1:8000 this is my api endpoint
@app.get("/")
def read_root():
    return {"Description": "Welcome to the celtics team library!"}

# get another function
@app.get("/jasontatum")
def read_root():
    return {"Description": "The personal stat of Jason Tatum in the game with Piston", "Points": 43, "Rebound": 10, "Assist": 3}

@app.get("/list-players")
async def list_players():
    return {"players": PLAYERS}

@app.get("/random-player")
async def random_player():
    return random.choice(PLAYERS)


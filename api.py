from fastapi import FastAPI, UploadFile, File, Body
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import shutil
import random

from main import open_bot
import json


# open_bot()



# приложение, которое все делает
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prices = [1, 2, 42]



class Pizza(BaseModel):
    name: str
    price: int
    image_path: str




@app.get('/prices')
async def responsePrices():
    prices = None
    with open("price.txt", "r") as my_file:
        prices = json.loads(my_file.read())
        print(prices)
    return prices
    # return 1



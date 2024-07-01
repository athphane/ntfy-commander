import asyncio
from random import randint

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from interfaces.tokens import Tokens
from interfaces.topics import Topics
from interfaces.users import Users

app = FastAPI()

origins = [
    'http://localhost:3001',
    'http://127.0.0.1:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/users/total')
async def users_total():
    await asyncio.sleep(randint(1, 1))
    return Users().total_count()


@app.get('/topics/total')
async def topics_total():
    await asyncio.sleep(randint(1, 1))
    return Topics().total_count()


@app.get('/tokens/total')
async def tokens_total():
    await asyncio.sleep(randint(1, 1))
    return Tokens().total_count()

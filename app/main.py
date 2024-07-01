import asyncio
from random import randint, random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3001'
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/users/total')
async def users_total():
    await asyncio.sleep(randint(1,1))
    return randint(1, 100)

@app.get('/topics/total')
async def topics_total():
    await asyncio.sleep(randint(1,1))
    return randint(1, 100)

@app.get('/tokens/total')
async def tokens_total():
    await asyncio.sleep(randint(1,1))
    return randint(1, 100)
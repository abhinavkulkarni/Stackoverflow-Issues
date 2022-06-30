import os

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index1():
    return {"message": "Welcome to my API 2!"}


@app.get("/index")
async def index2():
    myapi1_url = os.getenv("MYAPI1_URL")
    return RedirectResponse(url=f"{myapi1_url}/index")

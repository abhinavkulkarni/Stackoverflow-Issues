import os

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

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
    return RedirectResponse(url=f"{os.getenv('MYAPI1_URL')}/index")


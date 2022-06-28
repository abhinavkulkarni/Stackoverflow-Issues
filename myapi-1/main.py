from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
@app.get("/index")
async def index():
    return {"message": "Welcome to my API 1!"}

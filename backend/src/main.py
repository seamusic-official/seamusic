from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from music.router import music

app = FastAPI(
    title = "SeaMusic",
    description = "High-perfomance musical application"
)

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(music)
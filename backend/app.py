from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from db import Base, engine
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Brew Haven API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to Brew Haven API"}
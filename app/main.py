# main.py

from fastapi import FastAPI

from app.api.resume import router

app = FastAPI()
# create app

app.include_router(router, tags=["Resume"])
# register routes
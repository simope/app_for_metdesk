from fastapi import FastAPI
from .routes import router


my_app = FastAPI()
my_app.include_router(router)

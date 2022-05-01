from fastapi import FastAPI

from app.settings import router

from .settings import SettingsRouter
from .docker import ContainersRouter

app = FastAPI(openapi_url=None)

app.include_router(SettingsRouter)
app.include_router(ContainersRouter)

@app.get("/")
def root():
    return {"message": "Hello from Root!d"}
from fastapi import FastAPI

from app.docker.docker import DockerService

from . import settings
from . import containers

app = FastAPI(openapi_url=None)

app.include_router(settings.router)
app.include_router(containers.router)


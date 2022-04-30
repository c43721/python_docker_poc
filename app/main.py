from typing import Optional

from fastapi import FastAPI
import docker

app = FastAPI(openapi_url=None)
client = docker.from_env()

@app.get("/containers")
def read_containers(skip: int = 0, take: int = 10):
    containers = client.containers.list()

    returnData = {
        "count": len(containers),
        "data": [image.attrs for image in containers],
    }

    return returnData

@app.get("/images")
def get_images():
    images = client.images.list()

    returnData = {
        "count": len(images),
        "data": [image.attrs for image in images],
    }

    return returnData

from fastapi import Depends, FastAPI

from app.docker.docker import DockerService

app = FastAPI(openapi_url=None)

@app.get("/containers")
def get_settings(docker: DockerService = Depends()):
    containers = docker.get_all_running_containers()

    filtered = filter(lambda c: c.status == "running", containers)

    return {
        "containers": [containers.attrs for containers in filtered]
    }

@app.put("/settings")
def post_settings():
    return ""


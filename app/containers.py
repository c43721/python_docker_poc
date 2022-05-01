from fastapi import APIRouter, Depends

from app.docker.docker import DockerService

router = APIRouter(prefix="/containers")

@router.get("/containers")
def get_settings(docker: DockerService = Depends()):
    containers = docker.get_all_running_containers()

    filtered = filter(lambda c: c.status == "running", containers)

    return {
        "containers": [containers.attrs for containers in filtered]
    }


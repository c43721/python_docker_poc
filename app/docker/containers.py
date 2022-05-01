from fastapi import APIRouter, Depends

from app.docker.service import DockerService

router = APIRouter(prefix="/containers")

@router.get("/")
def get_settings(docker: DockerService = Depends()):
    containers = docker.get_all_running_containers()

    filtered = filter(lambda c: c.status == "running", containers)

    return {
        "containers": [containers.attrs for containers in filtered]
    }


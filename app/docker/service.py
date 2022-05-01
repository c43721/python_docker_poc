import docker

class DockerService:
    def __init__(self):
        self.client = docker.from_env()

    def get_client(self):
        return self.client

    def get_all_running_containers(self):
        return self.client.containers.list()

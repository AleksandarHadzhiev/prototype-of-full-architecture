import json
import requests
from fastapi import FastAPI, Request, Response, status
from config import load_config

class LoadBalancer:
    def __init__(self, servers: list[str]):
        self.servers = servers
        self.index =0

    def get_server(self) -> str:
        server = ""
        if self.index < len(self.servers) -1:
            server = self.servers[self.index]
            self.index += 1
        else:
            server = self.servers[self.index]
            self.index = 0
        return server

def create_app(env="dev"):
    config = load_config(env=env)
    targets: list[str] = config.TARGETS
    balancer = LoadBalancer(servers=targets)

    app = FastAPI()
    @app.get("/")
    def route(req: Request) -> Response:
        free_server = balancer.get_server()
        response = requests.get(f"{free_server}/aleks")
        body = response.json()
        return Response(content=json.dumps(body), status_code=status.HTTP_200_OK)
    return app

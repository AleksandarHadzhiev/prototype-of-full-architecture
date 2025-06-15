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
    @app.get("{path:path}")
    def get_request(path: str, req: Request) -> Response:
        free_server = balancer.get_server()
        response = requests.get(f"{free_server}{path}")
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)

    @app.post("{path:path}")
    async def post_request(path: str, request: Request) -> Response:
        free_server = balancer.get_server()
        data = await request.json()
        response = requests.post(f"{free_server}{path}", data=json.dumps(data))
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)

    @app.put("{path:path}")
    async def put_request(path: str, request: Request) -> Response:
        free_server = balancer.get_server()
        data = await request.json()
        response = requests.put(f"{free_server}{path}", data=json.dumps(data))
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)

    @app.delete("{path:path}")
    def delete_request(path: str, request: Request) -> Response:
        free_server = balancer.get_server()
        response = requests.delete(f"{free_server}{path}")
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)

    return app

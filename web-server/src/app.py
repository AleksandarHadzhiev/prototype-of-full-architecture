import json
import logging
import requests

from jinja2 import TemplateNotFound

from fastapi import FastAPI, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware 

from config import load_config

def create_app(env="dev"):
    templates = Jinja2Templates(directory="templates")
    config = load_config(env=env)
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins = config.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )

    @app.get("/")
    async def index():
        return Response(content=json.dumps({"message": "Everything booted up."}), status_code=status.HTTP_200_OK)

    @app.get("/{page}", response_class=HTMLResponse)
    async def route(page: str, request: Request):
        try:
            response = templates.TemplateResponse(
                request=request, name=f"{page}.html"
            )
            return response
        except TemplateNotFound:
            return templates.TemplateResponse(
                    request=request, name=f"not-found.html", status_code=status.HTTP_404_NOT_FOUND
                )

    @app.get("/backend/{path:path}")
    async def backend_get_request(path: str):
        response = requests.get(f"{config.BACKEND_URL}/{path}")
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)

    @app.post("/backend/{path:path}")
    async def backend_post_request(path: str, request: Request):
        data = await request.json()
        response = requests.post(f"{config.BACKEND_URL}/{path}", data=json.dumps(data))
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)


    @app.put("/backend/{path:path}")
    async def backend_put_request(path: str, request: Request):
        data = await request.json()
        response = requests.put(f"{config.BACKEND_URL}/{path}", data=json.dumps(data))
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)

    @app.delete("/backend/{path:path}")
    async def backend_delete_request(path: str):
        response = requests.delete(f"{config.BACKEND_URL}/{path}")
        body = response.json()
        return Response(content=json.dumps(body), status_code=response.status_code)

    return app
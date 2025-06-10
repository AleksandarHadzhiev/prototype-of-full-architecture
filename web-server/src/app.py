from jinja2 import TemplateNotFound
import uvicorn

from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 

def create_app(env="development"):
    templates = Jinja2Templates(directory="templates")

    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")


    @app.get("/{page}", response_class=HTMLResponse)
    async def route(page: str, request: Request):
        try:
            response = templates.TemplateResponse(
                request=request, name=f"{page}.html"
            )
            return response
        except TemplateNotFound as not_found:
            return templates.TemplateResponse(
                    request=request, name=f"not-found.html", status_code=status.HTTP_404_NOT_FOUND
                )

    return app
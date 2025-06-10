import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 


templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/{page}", response_class=HTMLResponse)
def route(page: str, request: Request):
    response = templates.TemplateResponse(
        request=request, name=f"{page}.html"
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app=app, port=3000)
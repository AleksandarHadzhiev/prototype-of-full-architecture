import json

from fastapi import FastAPI, Response, Request, status
from fastapi.middleware.cors import CORSMiddleware
from config import load_config

from src.tools.connection import Connection
from src.exceptions.create_todo_exceptions import EmptyTitleException, InvalidCompleteDateException, EmptyCompleteDateException, EmptyContentException
from src.todos.route import TodosRoute

def create_app(env="dev"):
    config = load_config(env=env)
    master = Connection()
    
    
    todos = TodosRoute(connection=master)
    
    app = FastAPI()

    slave_1_conn = Connection(port="59141")
    slave_2_conn = Connection(port="59142")

    app.add_middleware(
        CORSMiddleware,
        allow_origins = config.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )

    @app.exception_handler(EmptyTitleException)
    async def empty_title_exception_handler(requst: Request, exc: EmptyTitleException):
        return Response(content=json.dumps(exc.message),status_code=status.HTTP_400_BAD_REQUEST)

    @app.exception_handler(InvalidCompleteDateException)
    async def empty_title_exception_handler(requst: Request, exc: InvalidCompleteDateException):
        return Response(content=json.dumps(exc.message),status_code=status.HTTP_400_BAD_REQUEST)

    @app.exception_handler(EmptyContentException)
    async def empty_title_exception_handler(requst: Request, exc: EmptyContentException):
        return Response(content=json.dumps(exc.message),status_code=status.HTTP_400_BAD_REQUEST)

    @app.exception_handler(EmptyCompleteDateException)
    async def empty_title_exception_handler(requst: Request, exc: EmptyCompleteDateException):
        return Response(content=json.dumps(exc.message),status_code=status.HTTP_400_BAD_REQUEST)

    app.include_router(todos.router)

    @app.get('/')
    def index(request: Request):
        return Response(content=json.dumps({"message": "Everything booted up."}), status_code=status.HTTP_200_OK)
        
    @app.get("/{name}")
    def route(name: str, request: Request):
        if name.replace(" ", "") != "":
            message = f"Hello, {name}! Welcome to the app :)"
            return Response(content=json.dumps({"message": message}), status_code=status.HTTP_200_OK)
        else: return Response(content=json.dumps({"error": "Empty name"}), status_code=status.HTTP_400_BAD_REQUEST)

    return app
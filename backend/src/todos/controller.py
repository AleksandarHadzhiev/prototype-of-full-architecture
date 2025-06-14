import json

from fastapi import Response, status

from src.validations.create_todo_validation import CreateTodo
from src.tools.connection import Connection

class Controller():
    def __init__(self, conn: Connection):
        self.master_db = conn

    def create_todo(self, todo: CreateTodo) -> Response:
        data = todo
        return Response(content=json.dumps(data), status_code=status.HTTP_201_CREATED)
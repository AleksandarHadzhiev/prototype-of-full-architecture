from datetime import datetime
import json

from fastapi import Response, status

from src.validations.create_todo_validation import CreateTodo
from src.tools.connection import Connection
from src.todos.service import Service

class Controller():
    def __init__(self, conn: Connection):
        self.master_db = conn
        self.service = Service(master=conn)

    def create_todo(self, todo: CreateTodo) -> Response:
        self.service.create_todo(data=todo)
        return Response(content=json.dumps({"message": f"The task was created at {datetime.now()}"}), status_code=status.HTTP_201_CREATED)
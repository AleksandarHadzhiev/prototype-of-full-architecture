from datetime import datetime
import json

from fastapi import Response, status

from src.validations.create_todo_validation import CreateTodo
from src.tools.connections_balancer import ConnectionsBalancer
from src.todos.service import Service

class Controller():
    def __init__(self, balancer: ConnectionsBalancer):
        self.balancer = balancer
        self.service = Service(master=balancer.master_db)

    def create_todo(self, todo: CreateTodo) -> Response:
        self.service.create_todo(data=todo)
        return Response(content=json.dumps({"message": f"The task was created at {datetime.now()}"}), status_code=status.HTTP_201_CREATED)

    def get_todos(self) -> Response:
        free_read_connection = self.balancer.get_free_read_connection()
        todos = self.service.get_todos(conn=free_read_connection)
        return Response(
            content=json.dumps(todos), status_code=status.HTTP_200_OK
        )

    def edit_todo(self, todo: CreateTodo, id: int) -> Response:
        self.service.edit_todo(data=todo, id=id)
        return Response(content=json.dumps({"message": f"The task was created at {datetime.now()}"}), status_code=status.HTTP_201_CREATED)

    def complete_todo(self, id:int) -> Response:
        self.service.create_todo()
        return Response(content=json.dumps({"message": f"The task was created at {datetime.now()}"}), status_code=status.HTTP_201_CREATED)

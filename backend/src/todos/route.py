from fastapi.routing import APIRouter

from src.tools.connection import Connection
from src.todos.controller import Controller
class TodosRoute():
    def __init__(self, connection: Connection):
        self.router = APIRouter(prefix="/todos")
        self.controller = Controller(conn=connection)
        self.master_db = connection
        self.router.add_api_route("/", self.controller.create_todo, methods=["POST"])
        self.router.add_api_route("/", self.controller.get_todos, methods=["GET"])
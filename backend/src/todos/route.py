from fastapi.routing import APIRouter

from src.tools.connections_balancer import ConnectionsBalancer
from src.todos.controller import Controller
class TodosRoute():
    def __init__(self, balancer: ConnectionsBalancer):
        self.router = APIRouter(prefix="/todos")
        self.controller = Controller(balancer=balancer)
        self.router.add_api_route("/", self.controller.create_todo, methods=["POST"])
        self.router.add_api_route("/", self.controller.get_todos, methods=["GET"])
        self.router.add_api_route("/<id>", self.controller.edit_todo, methods=["PUT"])
        self.router.add_api_route("/<id>/complete", self.controller.complete_todo, methods=["PUT"])
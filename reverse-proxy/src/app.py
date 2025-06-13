import json
from fastapi import FastAPI, Request, Response, status

def create_app(env="dev"):
    print(env)
    app = FastAPI()

    @app.get("/")
    def index(req: Request) -> Response:
        return Response(content=json.dumps({"message": "Hello, World!"}), status_code=status.HTTP_200_OK)

    return app
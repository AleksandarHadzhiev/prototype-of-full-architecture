import json

from fastapi import FastAPI, Response, Request, status

def create_app(env="dev"):
    app = FastAPI()

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
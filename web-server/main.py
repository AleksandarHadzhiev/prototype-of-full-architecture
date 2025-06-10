import uvicorn

from src.app import create_app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app=app, port=3000)
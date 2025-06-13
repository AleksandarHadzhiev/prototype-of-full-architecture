import sys
import uvicorn

from src.app import create_app # to be added

n = len(sys.argv)
env = sys.argv[1]
host = sys.argv[2]
environments = ['docker', 'dev'] # to be added a config file for loading setup

if env in environments:
    app = create_app(env=env)
    uvicorn.run(app=app, host=host, port=8000)
import sys
import uvicorn

from src.main import create_app

n = len(sys.argv)
env = sys.argv[1]
host = sys.argv[2]
environments = ['docker', 'dev']
port = 8080

if sys.argv[3]:
    port = 8081

if env in environments:
    app = create_app(env=env)
    uvicorn.run(app=app, host=host,port=port)
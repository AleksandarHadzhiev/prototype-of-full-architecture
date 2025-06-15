class Config:
    ENV = ""
    BASE_URL = ""
    BACKEND_URL = ""
    ALLOWED_ORIGINS = []
    TARGETS = []

class DevConfig(Config):
    ENV = "dev"
    BASE_URL = "http://localhost:8000"
    ALLOWED_ORIGINS = "http://localhost:5000"
    TARGETS = ["http://localhost:8080"]

class DockerConfig(Config):
    ENV = "docker"
    BASE_URL = "http://localhost:8000"
    ALLOWED_ORIGINS = "http://localhost:5000"
    TARGETS = ["http://backend-1:8080"] # "http://backend-2:8080" - add to list for multiple
    

def load_config(env) -> Config:
    match env:
        case "dev":
            return DevConfig()
        case "docker":
            return DockerConfig()
        case _:
            return DevConfig()
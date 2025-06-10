class Config:
    ENV = ""
    BASE_URL = ""
    BACKEND_URL = ""
    ALLOWED_ORIGINS = []

class DevConfig(Config):
    ENV = "dev"
    BASE_URL = "127.0.0.1"
    BACKEND_URL = "127.0.0.1:8000"
    ALLOWED_ORIGINS = ["127.0.0.1:5000"]

class DockerConfig(Config):
    ENV = "docker"
    BASE_URL = "0.0.0.0"
    BACKEND_URL = "rev-proxy"
    ALLOWED_ORIGINS = ["forward-proxy"]

def load_config(env) -> Config:
    match env:
        case "dev":
            return DevConfig()
        case "docker":
            return DockerConfig()
        case _:
            return DevConfig()
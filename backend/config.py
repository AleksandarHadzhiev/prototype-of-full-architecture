class Config:
    ENV = ""
    BASE_URL = ""
    BACKEND_URL = ""
    ALLOWED_ORIGINS = []

class DevConfig(Config):
    ENV = "dev"
    BASE_URL = "http://localhost:8080"
    ALLOWED_ORIGINS = "http://localhost:8000"

class DockerConfig(Config):
    ENV = "docker"
    BASE_URL = "http://localhost:8080"
    ALLOWED_ORIGINS = "http://reverse-proxy:8000"

def load_config(env) -> Config:
    match env:
        case "dev":
            return DevConfig()
        case "docker":
            return DockerConfig()
        case _:
            return DevConfig()
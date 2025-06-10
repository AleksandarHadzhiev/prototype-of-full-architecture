class Config:
    ENV = ""
    BASE_URL = ""
    BACKEND_URL = ""
    ALLOWED_ORIGINS = []

class DevConfig(Config):
    ENV = "dev"
    BASE_URL = "127.0.0.1"
    ALLOWED_ORIGINS = ["http://localhost:3000",]

class DockerConfig(Config):
    ENV = "docker"
    BASE_URL = "http://localhost:8080"
    ALLOWED_ORIGINS = ["http://web-1:3000"]

def load_config(env) -> Config:
    match env:
        case "dev":
            return DevConfig()
        case "docker":
            return DockerConfig()
        case _:
            return DevConfig()
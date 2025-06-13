class Config:
    ENV = ""
    BASE_URL = ""
    BACKEND_URL = ""
    ALLOWED_ORIGINS = []
    POSTGRES_HOST = ""
    POSTGRES_DB = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    POSTGRES_MASTER_PORT = ""
    POSTGRES_SLAVE_ONE_PORT = ""
    POSTGRES_SLAVE_TWO_PORT = ""

class DevConfig(Config):
    ENV = "dev"
    BASE_URL = "http://localhost:8080"
    ALLOWED_ORIGINS = "http://localhost:8000"
    POSTGRES_HOST = "127.0.0.1"
    POSTGRES_DB = "todos"
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "postgres"
    POSTGRES_MASTER_PORT = "5432"
    POSTGRES_SLAVE_ONE_PORT = "5555"
    POSTGRES_SLAVE_TWO_PORT = "5556"

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
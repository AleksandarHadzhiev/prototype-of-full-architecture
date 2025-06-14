class Config:
    ENV = ""
    BASE_URL = ""
    BACKEND_URL = ""
    ALLOWED_ORIGINS = []
    POSTGRES_HOST_MASTER = ""
    POSTGRES_HOST_SLAVE_1 = ""
    POSTGRES_HOST_SLAVE_2 = ""
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
    POSTGRES_HOST_MASTER = "127.0.0.1"
    POSTGRES_HOST_SLAVE_1 = "127.0.0.1"
    POSTGRES_HOST_SLAVE_2 = "127.0.0.1"
    POSTGRES_DB = "todos"
    POSTGRES_USER = "dev"
    POSTGRES_PASSWORD = "dev"
    POSTGRES_MASTER_PORT = "5432"
    POSTGRES_SLAVE_ONE_PORT = "59141"
    POSTGRES_SLAVE_TWO_PORT = "59142"

class DockerConfig(Config):
    ENV = "docker"
    BASE_URL = "http://localhost:8080"
    ALLOWED_ORIGINS = "http://reverse-proxy:8000"
    POSTGRES_HOST_MASTER = "master"
    POSTGRES_HOST_SLAVE_1 = "slave_1"
    POSTGRES_HOST_SLAVE_2 = "slave_2"
    POSTGRES_DB = "todos"
    POSTGRES_USER = "dev"
    POSTGRES_PASSWORD = "dev"
    POSTGRES_MASTER_PORT = "5432"
    POSTGRES_SLAVE_ONE_PORT = "5432"
    POSTGRES_SLAVE_TWO_PORT = "5432"

def load_config(env) -> Config:
    match env:
        case "dev":
            return DevConfig()
        case "docker":
            return DockerConfig()
        case _:
            return DevConfig()
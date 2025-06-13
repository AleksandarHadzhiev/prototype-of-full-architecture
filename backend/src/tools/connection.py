import psycopg2

class Connection():
    def __init__(self, db: str="todos", host:str = "127.0.0.1", user: str="dev", password: str = "dev", port: str="5432"):
        self.connection = psycopg2.connect(
            database=db,
            host=host,
            user=user,
            port=port,
            password=password,
        )

    def get_conn(self):
        return self.connection
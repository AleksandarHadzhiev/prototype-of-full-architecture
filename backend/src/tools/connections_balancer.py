from src.tools.connection import Connection

class ConnectionsBalancer():
    def __init__(self, master_db: Connection):
        self.master_db = master_db
        self.index = 0
        self.read_connections: list[Connection] = []

    def add_read_connection(self, slave: Connection):
        self.read_connections(slave)
    
    def get_master(self):
        return self.master_db

    def get_free_read_connection(self):
        if self.index < len(self.read_connections) - 1:
            self.index+=1
        else:
            self.index = 0
        return self.read_connections[self.index]
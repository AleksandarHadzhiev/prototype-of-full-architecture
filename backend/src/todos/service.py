from datetime import datetime
from src.tools.connection import Connection
from src.validations.create_todo_validation import CreateTodo

class Service():
    def __init__(self, master: Connection):
        self.master = master


    def create_todo(self, data: CreateTodo):
        sql_statement = f"""
            INSERT INTO todos (id, title, content, date_created, date_completed, date_to_complete, status)
            VALUES (
                DEFAULT, '{data.title}', '{data.content}', '{datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}', DEFAULT, '{data.date_to_complete}', DEFAULT
            );
        """
        conn = self.master.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.commit()

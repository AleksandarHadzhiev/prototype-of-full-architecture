from datetime import datetime
from src.tools.connection import Connection
from src.validations.create_todo_validation import CreateTodo

class Service():
    def __init__(self, master: Connection):
        self.master = master

    def _execute_action(self, sql_statement: str):
        conn = self.master.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.commit()

    def complete_todo(self, id: int):
        sql_statement = f"""
            UPDATE todos SET 
                status = 'finished'
            WHERE id = {id};
        """
        self._execute_action(sql_statement=sql_statement)

    def edit_todo(self, data: CreateTodo, id: int):
        sql_statement = f"""
            UPDATE todos SET 
                title = '{data.title}',
                content = '{data.content}',
                date_to_complete = '{data.date_to_complete}'
            WHERE id = {id};
        """
        self._execute_action(sql_statement=sql_statement)

    def delete_todo(self, id: int):
        sql_statement = f"""
            DELETE FROM todos
            WHERE id = {id};
        """
        self._execute_action(sql_statement=sql_statement)

    def create_todo(self, data: CreateTodo):
        sql_statement = f"""
            INSERT INTO todos (id, title, content, date_created, date_completed, date_to_complete, status)
            VALUES (
                DEFAULT, '{data.title}', '{data.content}', '{datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}', DEFAULT, '{data.date_to_complete}', DEFAULT
            );
        """
        self._execute_action(sql_statement=sql_statement)

    def get_todos(self, conn: Connection):
        sql_statement = "SELECT * FROM todos"
        _conn = conn.get_conn()
        cursor = _conn.cursor()
        cursor.execute(sql_statement)
        todos = cursor.fetchall()
        if len(todos) > 0:
            _todos = []
            for todo in todos:
                _todo = self._format_todo(todo=todo)
                _todos.append(_todo)
            return _todos
        else:
            return []

    def _format_todo(self, todo):
        return {
            "id": todo[0],
            "title": todo[1],
            "content": todo[2],
            "date_created": todo[3],
            "date_completed": todo[4],
            "date_to_complete": todo[5],
            "status": todo[6],
        }
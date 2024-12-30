import sqlite3


DATABASE = "todos.db"

def init_db():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            priority TEXT NOT NULL,
            due_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_todo_db(name, description, priority, due_date):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO todos (name, description, priority, due_date)
        VALUES (?, ?, ?, ?)
    ''', (name, description, priority, due_date))
    conn.commit()
    conn.close()

def delete_todo_db(todo_id):
    """
    Delete a todo from the database by its ID.

    Args:
        todo_id (int): The ID of the todo to delete.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM todos
        WHERE id = ?
    ''', (todo_id,))
    conn.commit()
    conn.close()



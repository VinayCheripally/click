import sqlite3
import time
from datetime import datetime, timedelta
import pyttsx3

DATABASE = "todos.db"

def delete_overdue_todos():
    """Delete todos that are past their due date."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    now = datetime.now()
    
    cursor.execute('''
        DELETE FROM todos
        WHERE datetime(due_date) < ?
    ''', (now.strftime("%Y-%m-%d %H:%M:%S"),))
    
    conn.commit()
    conn.close()

def get_due_soon_todos():
    """Fetch todos that are due within the next 10 minutes."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    now = datetime.now()
    ten_minutes_later = now + timedelta(minutes=10)
    
    cursor.execute('''
        SELECT name, description, due_date
        FROM todos
        WHERE datetime(due_date) BETWEEN ? AND ?
    ''', (now.strftime("%Y-%m-%d %H:%M:%S"), ten_minutes_later.strftime("%Y-%m-%d %H:%M:%S")))
    
    todos = cursor.fetchall()
    conn.close()
    return todos

def alert_todos(todos):
    """Alert the user about the due todos using text-to-speech."""
    print(todos)
    engine = pyttsx3.init()
    for todo in todos:
        name, desc, due_date = todo
        message = f"Reminder: {name} is due at {due_date}. Description: {desc}"
        print(message)
        engine.say(message)
    engine.runAndWait()

def check_todos_periodically():
    while True:
        due_soon_todos = get_due_soon_todos()
        if due_soon_todos:
            alert_todos(due_soon_todos)
        delete_overdue_todos()
        time.sleep(30)  

if __name__ == "__main__":
    check_todos_periodically()


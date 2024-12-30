import sqlite3
import time
from datetime import datetime, timedelta
import pyttsx3
from twilio.rest import Client
from dotenv import load_dotenv
import os
from popup import popup_window_with_timeout
import threading

load_dotenv() 

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_sender = os.getenv("TWILIO_SENDER")
twilio_receiver = os.getenv('TWILIO_RECEIVER')

client = Client(account_sid, auth_token)

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
    engine = pyttsx3.init()
    def speak_message(text):
        engine.say(message)
        engine.runAndWait()
    for todo in todos:
        name, desc, due_date = todo
        message = f"Reminder: {name} is due at {due_date}. Description: {desc}"
        threading.Thread(target=speak_message,args=(message,)).start()
        if not popup_window_with_timeout(message):
            m = client.messages.create(
            body=message, 
            from_=twilio_sender,  
            to=twilio_receiver   
            )

def check_todos_periodically():
    try:
        while True:
            due_soon_todos = get_due_soon_todos()
            if due_soon_todos:
                alert_todos(due_soon_todos)
            delete_overdue_todos()
            time.sleep(300)  
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        exit(0)

if __name__ == "__main__":
    check_todos_periodically()


import sqlite3
import os

def log_error(message):
    db_path = os.path.join(os.getcwd(), 'lxc_deploy.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, message TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    cursor.execute('INSERT INTO logs (message) VALUES (?)', (message,))
    conn.commit()
    conn.close()
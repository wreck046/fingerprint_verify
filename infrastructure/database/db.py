import sqlite3
from config import DATABASE

def get_connection():

    return sqlite3.connect(DATABASE)


def init_db():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS verification_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        result TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        nik TEXT UNIQUE,
        template BLOB
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS verification_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        result TEXT
    )
    """)
    
    conn.commit()
    conn.close()
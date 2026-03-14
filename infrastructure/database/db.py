import sqlite3
from config import DATABASE


def get_connection():

    return sqlite3.connect(DATABASE)


def init_db():

    conn = get_connection()
    cur = conn.cursor()

    # users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        nik TEXT UNIQUE
    )
    """)

    cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_users_nik
        ON users(nik)
    """)

    # fingerprints table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fingerprints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        template BLOB
    )
    """)

    # verification logs
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
from scanner.scanner import capture
from database.db import get_connection

def register_user(name, nik):

    template = capture()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(name, nik, fingerprint_template) VALUES (?,?,?)",
        (name, nik, template)
    )

    conn.commit()
    conn.close()

    print("User berhasil terdaftar")
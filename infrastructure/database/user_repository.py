from core.entities import User

def find_by_nik(self, nik):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id,name,nik,template FROM users WHERE nik=?",
        (nik,)
    )

    row = cur.fetchone()
    conn.close()

    if row:
        return User(*row)

    return None

def log_verification(self, user_id, result):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO verification_logs(user_id,result) VALUES (?,?)",
        (user_id, result)
    )

    conn.commit()
    conn.close()
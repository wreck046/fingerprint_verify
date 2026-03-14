from core.entities import User
from infrastructure.database.db import get_connection


class UserRepository:

    def find_by_nik(self, nik):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT id,name,nik,template FROM users WHERE nik=?",
            (nik,)
        )

        row = cur.fetchone()
        conn.close()

        if not row:
            return None

        return User(*row)
    
    def log_verification(self, user_id, result):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO verification_logs(user_id,result) VALUES (?,?)",
            (user_id, result)
        )

        conn.commit()
        conn.close()

    def save_fingerprint(self, user_id, template):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO fingerprints(user_id,template) VALUES (?,?)",
            (user_id, template)
        )

        conn.commit()
        conn.close()

    def get_fingerprints(self, user_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT template FROM fingerprints WHERE user_id=?",
            (user_id,)
        )

        rows = cur.fetchall()
        conn.close()

        return [row[0] for row in rows]
    
    def get_all_users(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id,name,nik FROM users")

        rows = cur.fetchall()
        conn.close()

        return rows

    def get_logs(self):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        SELECT users.name, verification_logs.timestamp, verification_logs.result
        FROM verification_logs
        JOIN users ON users.id = verification_logs.user_id
        ORDER BY timestamp DESC
        """)

        rows = cur.fetchall()
        conn.close()

        return rows
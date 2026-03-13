from scanner.scanner import capture, connect
from database.db import get_connection
from config import MATCH_THRESHOLD


def verify_user(nik):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT name, fingerprint_template FROM users WHERE nik=?",
        (nik,)
    )

    user = cur.fetchone()

    if not user:
        print("NIK tidak ditemukan")
        return

    name, template = user

    probe = capture()

    f = connect()

    f.uploadCharacteristics(0x01, list(probe))
    f.uploadCharacteristics(0x02, list(template))

    score = f.compareCharacteristics()

    if score > MATCH_THRESHOLD:

        print("VERIFIED")
        print("Nama :", name)
        print("NIK :", nik)
        print("Score :", score)

    else:

        print("Fingerprint tidak cocok")
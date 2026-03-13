from database.db import get_user
from scanner.simulator import fake_fingerprint
from core.matcher import compare

THRESHOLD = 40

def verify_user(nik):

    user = get_user(nik)

    if not user:
        return "USER NOT FOUND"

    stored_template = user["template"]

    scanned_template = fake_fingerprint()

    score = compare(scanned_template, stored_template)

    if score > THRESHOLD:
        return "VERIFIED"

    return "NOT MATCH"
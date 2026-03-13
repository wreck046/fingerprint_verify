import hashlib
import random

def fake_fingerprint():

    seed = random.randint(1,100000)

    fp = hashlib.sha256(str(seed).encode()).digest()

    return fp
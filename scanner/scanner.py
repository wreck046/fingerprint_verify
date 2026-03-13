from pyfingerprint.pyfingerprint import PyFingerprint
from config import SERIAL_PORT, BAUDRATE

def connect():

    f = PyFingerprint(SERIAL_PORT, BAUDRATE, 0xFFFFFFFF, 0x00000000)

    if not f.verifyPassword():
        raise Exception("Fingerprint scanner tidak terdeteksi")

    return f


def capture():

    f = connect()

    print("Silakan letakkan jari...")

    while not f.readImage():
        pass

    f.convertImage(0x01)

    template = f.downloadCharacteristics(0x01)

    return bytes(template)
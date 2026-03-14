from pyfingerprint.pyfingerprint import PyFingerprint
from scanner.autodetect import detect_scanner
from config import BAUDRATE


class FingerprintScanner:

    MAX_RETRY = 3

    def __init__(self):

        port = detect_scanner()

        if not port:
            raise Exception("Fingerprint scanner not found")

        self.device = PyFingerprint(
            port,
            BAUDRATE,
            0xFFFFFFFF,
            0x00000000
        )

        if not self.device.verifyPassword():
            raise Exception("Scanner password verification failed")


    def capture(self):

        retry = 0

        while retry < self.MAX_RETRY:

            try:

                print("Place finger on scanner...")

                while not self.device.readImage():
                    pass

                self.device.convertImage(0x01)

                template = self.device.downloadCharacteristics(0x01)

                return bytes(template)

            except Exception as e:

                print("Capture error:", e)

                retry += 1

        raise Exception("Fingerprint capture failed after retries")
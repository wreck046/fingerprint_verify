from pyfingerprint.pyfingerprint import PyFingerprint
from config import SERIAL_PORT, BAUDRATE
from scanner.autodetect import detect_scanner

class FingerprintScanner:

    def __init__(self):

        port = detect_scanner()

        if not port:
            raise Exception("Scanner not found")

        self.device = PyFingerprint(
            port,
            BAUDRATE,
            0xFFFFFFFF,
            0x00000000
        )

        self.device = PyFingerprint(
            SERIAL_PORT,
            BAUDRATE,
            0xFFFFFFFF,
            0x00000000
        )

        if not self.device.verifyPassword():
            raise Exception("Scanner not detected")


    def capture(self):

        while not self.device.readImage():
            pass

        self.device.convertImage(0x01)

        template = self.device.downloadCharacteristics(0x01)

        return bytes(template)
    
    MAX_RETRY = 3

    def capture(self):
    
        retry = 0
    
        while retry < MAX_RETRY:
        
            try:
            
                while not self.device.readImage():
                    pass
                
                self.device.convertImage(0x01)
    
                template = self.device.downloadCharacteristics(0x01)
    
                return bytes(template)
    
            except Exception:
            
                retry += 1
    
        raise Exception("Fingerprint capture failed")
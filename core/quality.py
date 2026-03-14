class FingerprintQuality:

    MIN_LENGTH = 256  # sesuaikan dengan sensor/template size

    def is_good(self, template: bytes) -> bool:
        if not template:
            return False
        if len(template) < self.MIN_LENGTH:
            return False
        # cek variasi byte sederhana (hindari template “flat”)
        unique = len(set(template))
        return unique > 20
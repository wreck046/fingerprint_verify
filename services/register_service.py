from core.quality import FingerprintQuality

class RegisterService:

    ENROLL_COUNT = 3

    def __init__(self, scanner, repo):
        self.scanner = scanner
        self.repo = repo
        self.quality = FingerprintQuality()


    def register(self, name, nik):

        user_id = self.repo.create_user(name, nik)

        enrolled = 0
        while enrolled < self.ENROLL_COUNT:
            print(f"Scan fingerprint {enrolled+1}/{self.ENROLL_COUNT}")

            template = self.scanner.capture()

            if not self.quality.is_good(template):
                print("Fingerprint quality too low. Please scan again.")
                continue

            self.repo.save_fingerprint(user_id, template)
            enrolled += 1
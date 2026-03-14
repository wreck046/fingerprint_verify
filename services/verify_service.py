from core.matcher import FingerprintMatcher
from config import MATCH_THRESHOLD

class VerifyService:

    def __init__(self, scanner, repository):

        self.scanner = scanner
        self.repo = repository
        self.matcher = FingerprintMatcher()


    def verify(self, nik):

        user = self.repo.find_by_nik(nik)

        if not user:
            return None

        scanned_template = self.scanner.capture()

        score = self.matcher.compare(
            scanned_template,
            user.template
        )

        if score > MATCH_THRESHOLD:

            self.repo.log_verification(user.id, "SUCCESS")
        
            return user
        
        self.repo.log_verification(user.id, "FAILED")

        return None
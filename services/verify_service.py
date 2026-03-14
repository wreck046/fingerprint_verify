from core.matcher import FingerprintMatcher
from core.liveness import LivenessDetector
from config import MATCH_THRESHOLD

class VerifyService:

    def __init__(self, scanner, repo, matcher):
        self.scanner = scanner
        self.repo = repo
        self.matcher = matcher
        self.liveness = LivenessDetector()

    def verify(self, nik):

        user = self.repo.find_by_nik(nik)

        if not user:
            return None

        templates = self.repo.get_fingerprints(user.id)

        scanned = self.scanner.capture()

        # basic liveness check
        if not self.liveness.check(templates[0], scanned):
            print("Liveness detection failed")
            return None

        match, score = self.matcher.match(scanned, templates, threshold=0.6)

        if match:
            self.repo.log_verification(user.id, "SUCCESS")
            return user

        self.repo.log_verification(user.id, "FAILED")
        return None
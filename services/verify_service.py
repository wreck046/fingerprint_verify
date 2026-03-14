from core.matcher import FingerprintMatcher
from config import MATCH_THRESHOLD

class VerifyService:

    def __init__(self, scanner, repo, matcher):

        self.scanner = scanner
        self.repo = repo
        self.matcher = matcher


    def verify(self, nik):

        user = self.repo.find_by_nik(nik)

        if not user:
            return None

        templates = self.repo.get_fingerprints(user.id)

        scanned = self.scanner.capture()

        match, score = self.matcher.match(
            scanned,
            templates,
            threshold=0.6
        )

        if match:
            return user

        return None
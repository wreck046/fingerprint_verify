class RegisterService:

    ENROLL_COUNT = 3

    def __init__(self, scanner, repository):

        self.scanner = scanner
        self.repo = repository


    def register(self, name, nik):

        user_id = self.repo.create_user(name, nik)

        for i in range(self.ENROLL_COUNT):

            print(f"Scan fingerprint {i+1}/{self.ENROLL_COUNT}")

            template = self.scanner.capture()

            self.repo.save_fingerprint(user_id, template)

        print("Enrollment complete")
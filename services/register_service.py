class RegisterService:

    def __init__(self, scanner, repository):

        self.scanner = scanner
        self.repo = repository


    def register(self, name, nik):

        template = self.scanner.capture()

        self.repo.save(name, nik, template)
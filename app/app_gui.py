import tkinter as tk

from services.verify_service import VerifyService
from infrastructure.database.user_repository import UserRepository
from infrastructure.scanner.simulator import SimulatorScanner


repo = UserRepository()
scanner = SimulatorScanner()

service = VerifyService(scanner, repo)


def verify():

    nik = entry.get()

    result = service.verify(nik)

    if result:
        label.config(text="VERIFIED")
    else:
        label.config(text="NOT MATCH")


root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Verify", command=verify)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
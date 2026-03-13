import tkinter as tk
from services.fingerprint_service import verify_user

def verify():

    nik = entry.get()

    result = verify_user(nik)

    label_result.config(text=result)

root = tk.Tk()
root.title("Fingerprint Verification")

tk.Label(root,text="Masukkan NIK").pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root,text="Verify",command=verify)
btn.pack()

label_result = tk.Label(root,text="")
label_result.pack()

root.mainloop()
from database.db import init_db
from services.register_service import register_user
from services.verify_service import verify_user

init_db()

while True:

    print("\n=== SISTEM VERIFIKASI SIDIK JARI ===")
    print("1. Registrasi User")
    print("2. Verifikasi User")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":

        name = input("Nama: ")
        nik = input("NIK (No KTP): ")

        register_user(name, nik)

    elif menu == "2":

        nik = input("Masukkan NIK: ")

        verify_user(nik)

    elif menu == "3":
        break
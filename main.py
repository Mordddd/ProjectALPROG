from pathlib import Path
import json

from auth import login, register_voter
from kandidat import (
    tambah_kandidat,
    lihat_kandidat,
    edit_kandidat,
    hapus_kandidat,
    lihat_data_voter,
    cari_kandidat
)
from voting import vote_kandidat
from laporan import lihat_hasil_voting, lihat_detail_vote


DATA_FILE = Path(__file__).with_name("data.json")


def init_data():
    """Membuat file data.json jika belum tersedia."""
    if DATA_FILE.exists():
        return

    data_awal = {
        "users": [
            {
                "id": 1,
                "nama": "Administrator",
                "username": "admin",
                "password": "admin123",
                "role": "admin"
            }
        ],
        "kandidat": [],
        "votes": []
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data_awal, file, indent=4, ensure_ascii=False)


def pause():
    input("\nTekan ENTER untuk melanjutkan...")


def menu_utama():
    while True:
        print("\n=====================================")
        print("        SISTEM VOTING E-POLLING")
        print("=====================================")
        print("1. Login")
        print("2. Register Voter")
        print("3. Keluar")
        print("=====================================")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            user = login()
            if user is not None:
                if user["role"] == "admin":
                    menu_admin()
                elif user["role"] == "voter":
                    menu_voter(user)
                else:
                    print("\nRole user tidak dikenali.")
            pause()

        elif pilihan == "2":
            register_voter()
            pause()

        elif pilihan == "3":
            print("\nTerima kasih sudah menggunakan sistem voting.")
            break

        else:
            print("\nPilihan tidak valid!")
            pause()


def menu_admin():
    while True:
        print("\n=====================================")
        print("             MENU ADMIN")
        print("=====================================")
        print("1. Tambah Kandidat")
        print("2. Lihat Daftar Kandidat")
        print("3. Cari Kandidat")
        print("4. Edit Kandidat")
        print("5. Hapus Kandidat")
        print("6. Lihat Data Voter")
        print("7. Lihat Hasil Voting")
        print("8. Lihat Detail Vote")
        print("9. Logout")
        print("=====================================")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_kandidat()
            pause()

        elif pilihan == "2":
            lihat_kandidat()
            pause()

        elif pilihan == "3":
            cari_kandidat()
            pause()

        elif pilihan == "4":
            edit_kandidat()
            pause()

        elif pilihan == "5":
            hapus_kandidat()
            pause()

        elif pilihan == "6":
            lihat_data_voter()
            pause()

        elif pilihan == "7":
            lihat_hasil_voting()
            pause()

        elif pilihan == "8":
            lihat_detail_vote()
            pause()

        elif pilihan == "9":
            print("\nLogout dari menu admin.")
            break

        else:
            print("\nPilihan tidak valid!")
            pause()


def menu_voter(current_user):
    while True:
        print("\n=====================================")
        print("             MENU VOTER")
        print("=====================================")
        print("1. Lihat Daftar Kandidat")
        print("2. Cari Kandidat")
        print("3. Vote Kandidat")
        print("4. Lihat Hasil Voting")
        print("5. Logout")
        print("=====================================")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            lihat_kandidat()
            pause()

        elif pilihan == "2":
            cari_kandidat()
            pause()

        elif pilihan == "3":
            vote_kandidat(current_user)
            pause()

        elif pilihan == "4":
            lihat_hasil_voting()
            pause()

        elif pilihan == "5":
            print("\nLogout dari menu voter.")
            break

        else:
            print("\nPilihan tidak valid!")
            pause()


if __name__ == "__main__":
    init_data()
    menu_utama()

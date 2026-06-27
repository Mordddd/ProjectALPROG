from pathlib import Path
from datetime import datetime
import json

DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    if not DATA_FILE.exists():
        return {"users": [], "kandidat": [], "votes": []}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def cek_sudah_vote(user_id, votes):
    """Mengecek apakah user sudah melakukan voting."""
    for vote in votes:
        if vote["user_id"] == user_id:
            return True
    return False


def tampilkan_kandidat_singkat(kandidat_list):
    """Menampilkan kandidat dalam format singkat untuk voting."""
    print("\nDaftar Kandidat:")
    print("-------------------------------------")

    if not kandidat_list:
        print("Belum ada kandidat.")
        return

    for kandidat in kandidat_list:
        print(f"{kandidat['id']}. {kandidat['nama']}")


def vote_kandidat(current_user):
    """Proses voting kandidat oleh voter."""
    data = load_data()

    print("\n=====================================")
    print("            VOTE KANDIDAT")
    print("=====================================")

    if cek_sudah_vote(current_user["id"], data["votes"]):
        print("Maaf, Anda sudah melakukan voting.")
        print("Setiap voter hanya boleh memilih satu kali.")
        return

    if not data["kandidat"]:
        print("Belum ada kandidat yang tersedia.")
        return

    tampilkan_kandidat_singkat(data["kandidat"])

    try:
        kandidat_id = int(input("\nMasukkan ID kandidat yang dipilih: "))
    except ValueError:
        print("\nID kandidat harus berupa angka!")
        return

    kandidat_valid = False
    for kandidat in data["kandidat"]:
        if kandidat["id"] == kandidat_id:
            kandidat_valid = True
            break

    if not kandidat_valid:
        print("\nID kandidat tidak ditemukan!")
        return

    new_vote = {
        "user_id": current_user["id"],
        "kandidat_id": kandidat_id,
        "waktu_vote": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data["votes"].append(new_vote)
    save_data(data)

    print("\nVoting berhasil disimpan!")

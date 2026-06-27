from pathlib import Path
import json

DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    """Membaca data dari file JSON."""
    if not DATA_FILE.exists():
        return {"users": [], "kandidat": [], "votes": []}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    """Menyimpan data ke file JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_next_user_id(users):
    """Membuat ID user otomatis."""
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


def register_voter():
    """Mendaftarkan voter baru."""
    data = load_data()

    print("\n=====================================")
    print("           REGISTER VOTER")
    print("=====================================")

    nama = input("Nama Lengkap : ").strip()
    username = input("Username     : ").strip()
    password = input("Password     : ").strip()

    if not nama or not username or not password:
        print("\nData tidak boleh kosong!")
        return

    for user in data["users"]:
        if user["username"] == username:
            print("\nUsername sudah digunakan!")
            return

    new_user = {
        "id": get_next_user_id(data["users"]),
        "nama": nama,
        "username": username,
        "password": password,
        "role": "voter"
    }

    data["users"].append(new_user)
    save_data(data)

    print("\nAkun voter berhasil dibuat!")


def login():
    """Login user berdasarkan username dan password."""
    data = load_data()

    print("\n=====================================")
    print("                LOGIN")
    print("=====================================")

    username = input("Username : ").strip()
    password = input("Password : ").strip()

    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            print(f"\nLogin berhasil! Selamat datang, {user['nama']}.")
            print(f"Role: {user['role']}")
            return user

    print("\nLogin gagal! Username atau password salah.")
    return None

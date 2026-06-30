from pathlib import Path
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


def get_next_kandidat_id(kandidat_list):
    if not kandidat_list:
        return 1
    return max(kandidat["id"] for kandidat in kandidat_list) + 1


def lihat_kandidat():
    """Menampilkan daftar kandidat."""
    data = load_data()
    kandidat_list = data["kandidat"]

    print("\n=====================================")
    print("           DAFTAR KANDIDAT")
    print("=====================================")

    if not kandidat_list:
        print("Belum ada kandidat.")
        return

    for kandidat in kandidat_list:
        print(f"ID   : {kandidat['id']}")
        print(f"Nama : {kandidat['nama']}")
        print(f"Visi : {kandidat['visi']}")
        print(f"Misi : {kandidat['misi']}")
        print("-------------------------------------")


def tambah_kandidat():
    """Menambahkan kandidat baru."""
    data = load_data()

    print("\n=====================================")
    print("          TAMBAH KANDIDAT")
    print("=====================================")

    nama = input("Nama Kandidat : ").strip()
    visi = input("Visi          : ").strip()
    misi = input("Misi          : ").strip()

    if not nama:
        print("\nNama kandidat tidak boleh kosong!")
        return

    new_kandidat = {
        "id": get_next_kandidat_id(data["kandidat"]),
        "nama": nama,
        "visi": visi,
        "misi": misi
    }

    data["kandidat"].append(new_kandidat)
    save_data(data)

    print("\nData kandidat berhasil ditambahkan!")


def edit_kandidat():
    """Mengubah data kandidat berdasarkan ID."""
    data = load_data()

    lihat_kandidat()

    try:
        kandidat_id = int(input("\nMasukkan ID kandidat yang ingin diedit: "))
    except ValueError:
        print("\nID harus berupa angka!")
        return

    for kandidat in data["kandidat"]:
        if kandidat["id"] == kandidat_id:
            print("\nKosongkan input jika tidak ingin mengubah data.")
            nama_baru = input(f"Nama baru [{kandidat['nama']}]: ").strip()
            visi_baru = input(f"Visi baru [{kandidat['visi']}]: ").strip()
            misi_baru = input(f"Misi baru [{kandidat['misi']}]: ").strip()

            if nama_baru:
                kandidat["nama"] = nama_baru
            if visi_baru:
                kandidat["visi"] = visi_baru
            if misi_baru:
                kandidat["misi"] = misi_baru

            save_data(data)
            print("\nData kandidat berhasil diedit!")
            return

    print("\nKandidat dengan ID tersebut tidak ditemukan!")


def hapus_kandidat():
    """Menghapus kandidat berdasarkan ID."""
    data = load_data()

    lihat_kandidat()

    try:
        kandidat_id = int(input("\nMasukkan ID kandidat yang ingin dihapus: "))
    except ValueError:
        print("\nID harus berupa angka!")
        return

    kandidat_dipilih = None
    for kandidat in data["kandidat"]:
        if kandidat["id"] == kandidat_id:
            kandidat_dipilih = kandidat
            break

    if kandidat_dipilih is None:
        print("\nKandidat dengan ID tersebut tidak ditemukan!")
        return

    # Cek apakah kandidat sudah memiliki suara
    for vote in data["votes"]:
        if vote["kandidat_id"] == kandidat_id:
            print("\nKandidat tidak bisa dihapus karena sudah memiliki suara.")
            return

    data["kandidat"].remove(kandidat_dipilih)
    save_data(data)

    print("\nData kandidat berhasil dihapus!")


def lihat_data_voter():
    """Menampilkan semua user dengan role voter."""
    data = load_data()

    print("\n=====================================")
    print("             DATA VOTER")
    print("=====================================")

    voters = [user for user in data["users"] if user["role"] == "voter"]

    if not voters:
        print("Belum ada voter yang terdaftar.")
        return

    for voter in voters:
        status_vote = "Sudah Vote" if sudah_vote(voter["id"], data["votes"]) else "Belum Vote"
        print(f"ID       : {voter['id']}")
        print(f"Nama     : {voter['nama']}")
        print(f"Username : {voter['username']}")
        print(f"Status   : {status_vote}")
        print("-------------------------------------")


def sudah_vote(user_id, votes):
    for vote in votes:
        if vote["user_id"] == user_id:
            return True
    return False


def cari_kandidat():
    """Mencari Kandidat Berdasarkan Nama"""
    data = load_data()
    kandidat_list = data["kandidat"]

    print("\n=====================================")
    print("            CARI KANDIDAT")
    print("=====================================")

    if not kandidat_list:
        print("Belum ada kandidat.")
        return
    
    keyword = input("Masukkan nama kandidat yang dicari: ").strip().lower()

    if not keyword:
        print("\nKata kunci tidak boleh kosong!")
        return
    
    hasil = []

    for kandidat in kandidat_list:
        if keyword in kandidat["nama"].lower():
            hasil.append(kandidat)
    
    if not hasil:
        print("\nTidak ada kandidat yang ditemukan.")
        return
    
    print("\nHasil Pencarian:")
    print("-------------------------------------")
    for kandidat in hasil:
        print(f"ID   : {kandidat['id']}")
        print(f"Nama : {kandidat['nama']}")
        print(f"Visi : {kandidat['visi']}")
        print(f"Misi : {kandidat['misi']}")
        print("-------------------------------------")
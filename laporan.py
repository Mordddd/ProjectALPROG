from pathlib import Path
import json

DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    if not DATA_FILE.exists():
        return {"users": [], "kandidat": [], "votes": []}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def hitung_suara(kandidat_id, votes):
    total = 0
    for vote in votes:
        if vote["kandidat_id"] == kandidat_id:
            total += 1
    return total

def urutkan_hasil_voting(hasil):
    """
    Mengurutkan hasil voting berdasarkan jumlah suara terbanyak.
    Sorting menggunakan Bubble Sort secara descending.
    """
    n = len(hasil)

    for i in range(n):
        for j in range(0, n - i - 1):
            if hasil[j]["jumlah_suara"] < hasil[j + 1]["jumlah_suara"]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

    return hasil

def lihat_hasil_voting():
    """Menampilkan hasil voting setiap kandidat yang sudah diurutkan."""
    data = load_data()
    kandidat_list = data["kandidat"]
    votes = data["votes"]

    print("\n=====================================")
    print("            HASIL VOTING")
    print("      Urut Berdasarkan Suara")
    print("=====================================")

    if not kandidat_list:
        print("Belum ada kandidat.")
        return

    hasil = []

    for kandidat in kandidat_list:
        total_suara = hitung_suara(kandidat["id"], votes)

        hasil.append({
            "nama": kandidat["nama"],
            "jumlah_suara": total_suara
        })

    # Sorting hasil voting dari suara terbanyak ke terkecil
    hasil_terurut = urutkan_hasil_voting(hasil)

    print(f"{'No':<4}{'Nama Kandidat':<25}{'Jumlah Suara'}")
    print("-------------------------------------")

    for index, item in enumerate(hasil_terurut, start=1):
        print(f"{index:<4}{item['nama']:<25}{item['jumlah_suara']}")

    print("-------------------------------------")
    print(f"Total Suara Masuk: {len(votes)}")


def lihat_detail_vote():
    """Menampilkan detail voter dan kandidat yang dipilih. Cocok untuk admin."""
    data = load_data()

    print("\n=====================================")
    print("           DETAIL DATA VOTE")
    print("=====================================")

    if not data["votes"]:
        print("Belum ada data voting.")
        return

    for vote in data["votes"]:
        user = cari_user_by_id(vote["user_id"], data["users"])
        kandidat = cari_kandidat_by_id(vote["kandidat_id"], data["kandidat"])

        nama_user = user["nama"] if user else "User tidak ditemukan"
        nama_kandidat = kandidat["nama"] if kandidat else "Kandidat tidak ditemukan"

        print(f"Voter     : {nama_user}")
        print(f"Kandidat  : {nama_kandidat}")
        print(f"Waktu     : {vote.get('waktu_vote', '-')}")
        print("-------------------------------------")


def cari_user_by_id(user_id, users):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def cari_kandidat_by_id(kandidat_id, kandidat_list):
    for kandidat in kandidat_list:
        if kandidat["id"] == kandidat_id:
            return kandidat
    return None

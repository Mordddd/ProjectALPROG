# Sistem Voting / E-Polling Berbasis Python Console

## Deskripsi Proyek

Sistem Voting / E-Polling adalah aplikasi berbasis console yang dibuat menggunakan bahasa pemrograman Python. Aplikasi ini digunakan untuk membantu proses pemilihan kandidat secara sederhana, seperti pemilihan ketua kelas, ketua kelompok, atau pemilihan internal organisasi.

Sistem ini memiliki dua jenis pengguna, yaitu **Admin** dan **Voter**. Admin dapat mengelola data kandidat, melihat data voter, melihat hasil voting, dan melihat detail vote. Voter dapat melakukan registrasi, login, melihat kandidat, mencari kandidat, melakukan voting, dan melihat hasil voting.

Data pada sistem ini disimpan secara lokal menggunakan file `data.json`, sehingga tidak memerlukan database eksternal.

---

## Fitur Utama

* Register voter baru
* Login admin dan voter
* Role user: admin dan voter
* Tambah kandidat
* Lihat daftar kandidat
* Cari kandidat menggunakan Linear Search
* Edit data kandidat
* Hapus data kandidat
* Voting kandidat
* Validasi satu voter hanya dapat memilih satu kali
* Lihat hasil voting
* Sorting hasil voting berdasarkan jumlah suara terbanyak
* Lihat data voter
* Lihat detail vote

---

## Struktur Folder

```text
ProjectAkhirALPROG/
│
├── main.py
├── auth.py
├── kandidat.py
├── voting.py
├── laporan.py
└── data.json
```

Keterangan file:

| File          | Fungsi                                                                         |
| ------------- | ------------------------------------------------------------------------------ |
| `main.py`     | File utama untuk menjalankan program dan menampilkan menu                      |
| `auth.py`     | Mengatur proses login dan register voter                                       |
| `kandidat.py` | Mengatur data kandidat, termasuk tambah, lihat, edit, hapus, dan cari kandidat |
| `voting.py`   | Mengatur proses voting kandidat                                                |
| `laporan.py`  | Menampilkan hasil voting, detail vote, dan sorting hasil voting                |
| `data.json`   | Menyimpan data user, kandidat, dan hasil vote secara lokal                     |


## Struktur Data

Sistem ini menggunakan beberapa struktur data utama:

### 1. Dictionary

Dictionary digunakan untuk menyimpan data dalam bentuk pasangan key-value.

Contoh data user:

```python
{
    "id": 1,
    "nama": "Administrator",
    "username": "admin",
    "password": "admin123",
    "role": "admin"
}
```

Contoh data kandidat:

```python
{
    "id": 1,
    "nama": "Andi Pratama",
    "visi": "Mewujudkan organisasi yang aktif dan transparan",
    "misi": "Meningkatkan komunikasi dan kegiatan positif"
}
```

### 2. List

List digunakan untuk menyimpan kumpulan data, seperti daftar user, daftar kandidat, dan daftar vote.

Contoh:

```json
{
    "users": [],
    "kandidat": [],
    "votes": []
}
```

### 3. JSON

File `data.json` digunakan sebagai penyimpanan lokal agar data tetap tersimpan walaupun program ditutup.


## Algoritma yang Digunakan

### 1. Linear Search

Linear Search digunakan pada fitur pencarian kandidat. Sistem akan memeriksa nama kandidat satu per satu berdasarkan keyword yang dimasukkan oleh user.

Contoh proses:

```text
Input keyword
Periksa kandidat pertama
Periksa kandidat kedua
Periksa kandidat berikutnya
Jika nama kandidat cocok, tampilkan hasil
```

Kompleksitas waktu Linear Search adalah:

```text
O(n)
```

Karena sistem mencari data satu per satu dari daftar kandidat.


### 2. Sorting Hasil Voting

Sorting digunakan untuk mengurutkan hasil voting berdasarkan jumlah suara terbanyak. Kandidat dengan suara paling banyak akan ditampilkan di posisi paling atas.

Algoritma sorting yang digunakan adalah Bubble Sort secara descending.

Kompleksitas waktu Bubble Sort adalah:

```text
O(n²)
```


### 3. Counting Vote

Counting digunakan untuk menghitung jumlah suara setiap kandidat. Sistem akan membandingkan `kandidat_id` pada data vote dengan ID kandidat yang tersedia.


## Akun Admin Default

Gunakan akun berikut untuk masuk sebagai admin:

```text
Username : admin
Password : admin123
```

Admin dapat mengelola kandidat, melihat data voter, melihat detail vote, dan melihat hasil voting.

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall di komputer.
2. Buka folder project di VS Code atau terminal.
3. Jalankan file `main.py`.

Perintah terminal:

```bash
python main.py
```

Atau jika menggunakan Windows dan perintah `python` tidak berjalan:

```bash
py main.py
```


## Alur Penggunaan Program

### Sebagai Admin

1. Jalankan program.
2. Pilih menu `Login`.
3. Masukkan username dan password admin.
4. Setelah masuk ke menu admin, admin dapat:

   * Menambah kandidat
   * Melihat kandidat
   * Mencari kandidat
   * Mengedit kandidat
   * Menghapus kandidat
   * Melihat data voter
   * Melihat hasil voting
   * Melihat detail vote

### Sebagai Voter

1. Jalankan program.
2. Pilih menu `Register Voter`.
3. Masukkan nama, username, dan password.
4. Login menggunakan akun voter yang sudah dibuat.
5. Setelah masuk ke menu voter, voter dapat:

   * Melihat daftar kandidat
   * Mencari kandidat
   * Melakukan voting
   * Melihat hasil voting

Catatan: Setiap voter hanya dapat melakukan voting satu kali.


## Contoh Tampilan Menu

### Menu Utama

```text
=====================================
        SISTEM VOTING E-POLLING
=====================================
1. Login
2. Register Voter
3. Keluar
=====================================
Pilih menu:
```

### Menu Admin

```text
=====================================
             MENU ADMIN
=====================================
1. Tambah Kandidat
2. Lihat Daftar Kandidat
3. Cari Kandidat
4. Edit Kandidat
5. Hapus Kandidat
6. Lihat Data Voter
7. Lihat Hasil Voting
8. Lihat Detail Vote
9. Logout
=====================================
Pilih menu:
```

### Menu Voter

```text
=====================================
             MENU VOTER
=====================================
1. Lihat Daftar Kandidat
2. Cari Kandidat
3. Vote Kandidat
4. Lihat Hasil Voting
5. Logout
=====================================
Pilih menu:
```


## Validasi dan Error Handling

Sistem memiliki beberapa validasi sederhana, yaitu:

* Username tidak boleh kosong.
* Password tidak boleh kosong.
* Username yang sudah digunakan tidak dapat didaftarkan ulang.
* Login gagal jika username atau password salah.
* ID kandidat harus berupa angka.
* Voter hanya dapat melakukan voting satu kali.
* Sistem menampilkan pesan jika kandidat tidak ditemukan.
* Sistem menampilkan pesan jika belum ada kandidat.
* Sistem menampilkan pesan jika data voting masih kosong.


## Kelebihan Sistem

* Program sederhana dan mudah digunakan.
* Tidak membutuhkan database eksternal.
* Data tersimpan secara lokal menggunakan file JSON.
* Memiliki pembagian role admin dan voter.
* Menggunakan modular programming.
* Mengimplementasikan Linear Search.
* Mengimplementasikan Sorting hasil voting.
* Cocok untuk proyek akhir mata kuliah Algoritma dan Pemrograman.


## Keterbatasan Sistem

* Sistem masih berbasis console.
* Password belum dienkripsi.
* Data JSON masih dapat diedit secara manual.
* Belum memiliki tampilan GUI.
* Belum mendukung multi-event voting.
* Belum menggunakan database eksternal.


## Rencana Pengembangan

Beberapa pengembangan yang dapat dilakukan di masa depan:

* Menambahkan enkripsi password.
* Menggunakan database SQLite atau MySQL.
* Membuat tampilan GUI.
* Menambahkan fitur export hasil voting.
* Menambahkan fitur multi-event voting.
* Menambahkan grafik hasil voting.


## Identitas Proyek

* Nama Proyek: Sistem Voting / E-Polling
* Bahasa Pemrograman: Python
* Jenis Aplikasi: Console-Based Application
* Penyimpanan Data: JSON File
* Mata Kuliah: Algoritma dan Pemrograman
* Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.
* Semester: Genap 2025/2026


## Developer

Nama: Muhamad Qeisha Kamil Ibrahim
NIM: 0112524022
Kelas: Algoritma Pemrograman
Program Studi: Informatika
Universitas: Universitas Al Azhar Indonesia

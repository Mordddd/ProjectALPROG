# Manual Testing

## Sistem Voting / E-Polling Berbasis Python Console

## 1. Tujuan Pengujian

Pengujian manual dilakukan untuk memastikan bahwa setiap fitur pada Sistem Voting / E-Polling berjalan sesuai dengan kebutuhan. Pengujian ini dilakukan dengan menjalankan program melalui console dan mencoba setiap menu yang tersedia, baik sebagai admin maupun voter.

---

## 2. Lingkungan Pengujian

| Komponen           | Keterangan                |
| ------------------ | ------------------------- |
| Bahasa Pemrograman | Python                    |
| Jenis Aplikasi     | Console-Based Application |
| Penyimpanan Data   | JSON File                 |
| File Utama         | `main.py`                 |
| Sistem Operasi     | Windows                   |
| Editor             | Visual Studio Code        |

---

## 3. Akun Pengujian

### Akun Admin

| Username | Password | Role  |
| -------- | -------- | ----- |
| admin    | admin123 | admin |

### Akun Voter Contoh

| Nama       | Username | Password | Role  |
| ---------- | -------- | -------- | ----- |
| Voter Satu | voter1   | voter123 | voter |
| Voter Dua  | voter2   | voter123 | voter |

---

## 4. Tabel Pengujian Manual

| No | Test Case                             | Langkah Pengujian                                         | Input                                                        | Expected Output                                         | Actual Output                                           | Status |
| -- | ------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------- | ------ |
| 1  | Menjalankan program                   | Jalankan file `main.py` melalui terminal                  | `python main.py`                                             | Menu utama tampil                                       | Menu utama tampil                                       | PASS   |
| 2  | Login admin berhasil                  | Pilih menu Login, masukkan akun admin                     | Username: `admin`, Password: `admin123`                      | Admin berhasil login dan masuk ke menu admin            | Admin berhasil login dan masuk ke menu admin            | PASS   |
| 3  | Login gagal                           | Pilih menu Login, masukkan password salah                 | Username: `admin`, Password: `salah`                         | Sistem menampilkan pesan login gagal                    | Sistem menampilkan pesan login gagal                    | PASS   |
| 4  | Register voter baru                   | Pilih menu Register Voter dan isi data                    | Nama: `Voter Satu`, Username: `voter1`, Password: `voter123` | Akun voter berhasil dibuat                              | Akun voter berhasil dibuat                              | PASS   |
| 5  | Register username duplikat            | Register menggunakan username yang sudah ada              | Username: `voter1`                                           | Sistem menolak username duplikat                        | Sistem menolak username duplikat                        | PASS   |
| 6  | Login voter berhasil                  | Login menggunakan akun voter                              | Username: `voter1`, Password: `voter123`                     | Voter berhasil login dan masuk ke menu voter            | Voter berhasil login dan masuk ke menu voter            | PASS   |
| 7  | Admin menambah kandidat               | Login admin, pilih Tambah Kandidat                        | Nama: `Andi Pratama`, Visi: `Jujur`, Misi: `Aktif`           | Kandidat berhasil ditambahkan                           | Kandidat berhasil ditambahkan                           | PASS   |
| 8  | Admin melihat daftar kandidat         | Login admin, pilih Lihat Daftar Kandidat                  | Pilihan menu `2`                                             | Sistem menampilkan daftar kandidat                      | Sistem menampilkan daftar kandidat                      | PASS   |
| 9  | Admin mencari kandidat                | Login admin, pilih Cari Kandidat                          | Keyword: `Andi`                                              | Sistem menampilkan kandidat yang sesuai                 | Sistem menampilkan kandidat yang sesuai                 | PASS   |
| 10 | Cari kandidat tidak ditemukan         | Pilih Cari Kandidat dengan keyword yang tidak ada         | Keyword: `XYZ`                                               | Sistem menampilkan pesan kandidat tidak ditemukan       | Sistem menampilkan pesan kandidat tidak ditemukan       | PASS   |
| 11 | Admin mengedit kandidat               | Login admin, pilih Edit Kandidat                          | ID kandidat valid, data baru                                 | Data kandidat berhasil diedit                           | Data kandidat berhasil diedit                           | PASS   |
| 12 | Admin menghapus kandidat              | Login admin, pilih Hapus Kandidat                         | ID kandidat valid                                            | Data kandidat berhasil dihapus                          | Data kandidat berhasil dihapus                          | PASS   |
| 13 | Edit kandidat dengan ID tidak valid   | Pilih Edit Kandidat, masukkan ID yang tidak tersedia      | ID: `999`                                                    | Sistem menampilkan kandidat tidak ditemukan             | Sistem menampilkan kandidat tidak ditemukan             | PASS   |
| 14 | Input ID bukan angka                  | Pada fitur edit/hapus/vote, masukkan teks                 | ID: `abc`                                                    | Sistem menampilkan pesan ID harus berupa angka          | Sistem menampilkan pesan ID harus berupa angka          | PASS   |
| 15 | Voter melihat daftar kandidat         | Login voter, pilih Lihat Daftar Kandidat                  | Pilihan menu `1`                                             | Sistem menampilkan daftar kandidat                      | Sistem menampilkan daftar kandidat                      | PASS   |
| 16 | Voter mencari kandidat                | Login voter, pilih Cari Kandidat                          | Keyword: `Andi`                                              | Sistem menampilkan kandidat yang sesuai                 | Sistem menampilkan kandidat yang sesuai                 | PASS   |
| 17 | Voter melakukan voting                | Login voter, pilih Vote Kandidat                          | ID kandidat valid                                            | Voting berhasil disimpan                                | Voting berhasil disimpan                                | PASS   |
| 18 | Voter voting dua kali                 | Login voter yang sudah pernah voting, pilih Vote Kandidat | ID kandidat valid                                            | Sistem menolak voting kedua                             | Sistem menolak voting kedua                             | PASS   |
| 19 | Voting dengan ID kandidat tidak valid | Login voter baru, pilih Vote Kandidat                     | ID: `999`                                                    | Sistem menampilkan ID kandidat tidak ditemukan          | Sistem menampilkan ID kandidat tidak ditemukan          | PASS   |
| 20 | Melihat hasil voting                  | Pilih menu Lihat Hasil Voting                             | Pilihan menu hasil voting                                    | Sistem menampilkan jumlah suara tiap kandidat           | Sistem menampilkan jumlah suara tiap kandidat           | PASS   |
| 21 | Sorting hasil voting                  | Lihat hasil voting setelah beberapa voter memilih         | Data vote beberapa kandidat                                  | Kandidat dengan suara terbanyak tampil di atas          | Kandidat dengan suara terbanyak tampil di atas          | PASS   |
| 22 | Admin melihat data voter              | Login admin, pilih Lihat Data Voter                       | Pilihan menu data voter                                      | Sistem menampilkan daftar voter dan status voting       | Sistem menampilkan daftar voter dan status voting       | PASS   |
| 23 | Admin melihat detail vote             | Login admin, pilih Lihat Detail Vote                      | Pilihan menu detail vote                                     | Sistem menampilkan nama voter, kandidat, dan waktu vote | Sistem menampilkan nama voter, kandidat, dan waktu vote | PASS   |
| 24 | Logout admin                          | Pada menu admin, pilih Logout                             | Pilihan menu logout                                          | Sistem kembali ke menu utama                            | Sistem kembali ke menu utama                            | PASS   |
| 25 | Logout voter                          | Pada menu voter, pilih Logout                             | Pilihan menu logout                                          | Sistem kembali ke menu utama                            | Sistem kembali ke menu utama                            | PASS   |
| 26 | Keluar program                        | Pada menu utama, pilih Keluar                             | Pilihan menu `3`                                             | Program berhenti                                        | Program berhenti                                        | PASS   |

---

## 5. Pengujian Error Handling

| No | Kondisi Error                               | Input                         | Penanganan Sistem                                           | Status |
| -- | ------------------------------------------- | ----------------------------- | ----------------------------------------------------------- | ------ |
| 1  | Login dengan data salah                     | Username/password salah       | Sistem menampilkan pesan login gagal                        | PASS   |
| 2  | Register dengan data kosong                 | Nama/username/password kosong | Sistem menampilkan pesan data tidak boleh kosong            | PASS   |
| 3  | Register username yang sudah digunakan      | Username sama                 | Sistem menampilkan pesan username sudah digunakan           | PASS   |
| 4  | Input ID kandidat bukan angka               | `abc`                         | Sistem menampilkan pesan ID harus berupa angka              | PASS   |
| 5  | Vote menggunakan ID kandidat yang tidak ada | `999`                         | Sistem menampilkan pesan ID kandidat tidak ditemukan        | PASS   |
| 6  | Voter melakukan vote lebih dari satu kali   | Vote kedua                    | Sistem menampilkan pesan bahwa voter sudah melakukan voting | PASS   |
| 7  | Mencari kandidat dengan keyword kosong      | Input kosong                  | Sistem menampilkan pesan keyword tidak boleh kosong         | PASS   |
| 8  | Menampilkan kandidat saat data kosong       | Tidak ada kandidat            | Sistem menampilkan pesan belum ada kandidat                 | PASS   |
| 9  | Melihat detail vote saat belum ada vote     | Tidak ada data vote           | Sistem menampilkan pesan belum ada data voting              | PASS   |


## 6. Kesimpulan Pengujian

Berdasarkan hasil pengujian manual, seluruh fitur utama pada Sistem Voting / E-Polling dapat berjalan sesuai dengan kebutuhan. Fitur login, register, manajemen kandidat, pencarian kandidat, voting, validasi satu voter hanya dapat memilih satu kali, hasil voting, sorting hasil voting, dan detail vote berhasil diuji.

Sistem juga sudah memiliki beberapa validasi dan error handling sederhana, seperti penolakan login salah, username duplikat, input ID bukan angka, kandidat tidak ditemukan, dan pencegahan voting lebih dari satu kali.

Dengan demikian, sistem dinyatakan berjalan dengan baik untuk kebutuhan proyek akhir Algoritma dan Pemrograman berbasis Python console.

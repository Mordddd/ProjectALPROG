# AI Usage Log — Proyek Akhir

## Identitas

Nama: Muhamad Qeisha Kamil Ibrahim
NIM: 0112524022
Kelas: Algoritma Pemrograma
Mata Kuliah: Algoritma dan Pemrograman
Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.
Judul Proyek: Sistem Voting / E-Polling Berbasis Python Console


## Ringkasan Penggunaan AI

Dalam pengerjaan proyek akhir ini, AI digunakan sebagai alat bantu untuk membantu proses perancangan awal dan penyelesaian masalah selama pengembangan aplikasi. AI digunakan sebagai referensi untuk menyusun rancangan sistem, bukan sebagai pengganti pemahaman terhadap kode program.

Bagian yang dibantu oleh AI meliputi:

1. Perancangan struktur folder proyek.
2. Pembuatan desain top-down sistem.
3. Pembuatan pseudocode.
4. Pembuatan sketsa user interface berbasis console.
5. Membantu debugging ketika terjadi error program.

Seluruh hasil akhir tetap dipelajari, disesuaikan, dan diuji kembali agar sesuai dengan kebutuhan proyek Sistem Voting / E-Polling.


## Detail Penggunaan AI

### 1. Perancangan Struktur Folder Proyek

Prompt yang digunakan:

```text
Buatkan struktur dasar project Sistem Voting / E-Polling berbasis Python.
```

Bantuan yang diberikan AI:

AI memberikan saran pembagian file program agar proyek lebih rapi dan modular. Struktur yang disarankan terdiri dari beberapa file, yaitu file utama, file autentikasi, file kandidat, file voting, file laporan, dan file penyimpanan data.

Hasil yang digunakan:

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

Penyesuaian yang dilakukan:

Struktur tersebut digunakan karena sesuai dengan kebutuhan proyek. Setiap file memiliki fungsi masing-masing agar program lebih mudah dipahami dan dikembangkan.

Pelajaran yang didapat:

Saya memahami bahwa program yang cukup besar sebaiknya tidak ditulis dalam satu file saja, melainkan dibagi menjadi beberapa modul agar lebih rapi.


### 2. Pembuatan Desain Top-Down

Prompt yang digunakan:

```text
Buatkan desain top-down untuk Sistem Voting / E-Polling.
```

Bantuan yang diberikan AI:

AI membantu memecah sistem menjadi beberapa bagian utama, yaitu manajemen data lokal, autentikasi user, menu admin, menu voter, dan laporan hasil voting.

Hasil yang digunakan:

```text
SISTEM VOTING / E-POLLING
│
├── Manajemen Data Lokal
│   ├── Membaca data
│   ├── Menyimpan data
│   └── Mengelola file data.json
│
├── Autentikasi User
│   ├── Register voter
│   ├── Login user
│   └── Cek role user
│
├── Menu Admin
│   ├── Tambah kandidat
│   ├── Lihat kandidat
│   ├── Cari kandidat
│   ├── Edit kandidat
│   ├── Hapus kandidat
│   ├── Lihat data voter
│   └── Lihat hasil voting
│
├── Menu Voter
│   ├── Lihat kandidat
│   ├── Cari kandidat
│   ├── Vote kandidat
│   └── Lihat hasil voting
│
└── Laporan
    ├── Hitung suara
    ├── Urutkan hasil voting
    └── Tampilkan hasil voting
```

Penyesuaian yang dilakukan:

Desain top-down disesuaikan dengan fitur akhir proyek, seperti fitur pencarian kandidat dan sorting hasil voting.

Pelajaran yang didapat:

Saya memahami bahwa desain top-down membantu memecah masalah besar menjadi bagian-bagian kecil yang lebih mudah dikerjakan.


### 3. Pembuatan Pseudocode

Prompt yang digunakan:

```text
Buatkan pseudocode untuk alur Sistem Voting / E-Polling.
```

Bantuan yang diberikan AI:

AI membantu menyusun pseudocode untuk menu utama, menu admin, menu voter, dan proses voting.

Hasil yang digunakan:

```text
START

Tampilkan menu utama:
1. Login
2. Register Voter
3. Keluar

Jika memilih Login:
    Input username dan password
    Cek data user

    Jika login valid:
        Jika role admin:
            Tampilkan menu admin
        Jika role voter:
            Tampilkan menu voter
    Jika login tidak valid:
        Tampilkan pesan login gagal

Jika memilih Register:
    Input nama, username, dan password
    Simpan data voter

Jika memilih Keluar:
    Program selesai

END
```

Pseudocode voting:

```text
START

Cek apakah voter sudah pernah vote

Jika sudah:
    Tampilkan pesan bahwa voter sudah melakukan voting

Jika belum:
    Tampilkan daftar kandidat
    Input ID kandidat
    Jika ID kandidat valid:
        Simpan vote
        Tampilkan pesan voting berhasil
    Jika ID kandidat tidak valid:
        Tampilkan pesan kandidat tidak ditemukan

END
```

Penyesuaian yang dilakukan:

Pseudocode disesuaikan dengan fitur yang benar-benar dibuat di program, seperti validasi satu voter hanya boleh memilih satu kali.

Pelajaran yang didapat:

Saya memahami bahwa pseudocode membantu menjelaskan alur program sebelum diterjemahkan menjadi kode Python.


### 4. Pembuatan Sketsa User Interface Console

Prompt yang digunakan:

```text
Buatkan sketsa desain user interface console-based untuk Sistem Voting / E-Polling.
```

Bantuan yang diberikan AI:

AI membantu membuat contoh tampilan menu berbasis console, seperti menu utama, menu admin, menu voter, tampilan voting, dan tampilan hasil voting.

Hasil yang digunakan:

Menu utama:

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

Menu admin:

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

Menu voter:

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

Penyesuaian yang dilakukan:

Sketsa UI disesuaikan dengan menu akhir yang ada di program agar tampilan console lebih rapi dan mudah dipahami.

Pelajaran yang didapat:

Saya memahami bahwa meskipun program berbasis console, tampilan tetap perlu dirancang agar pengguna mudah memahami pilihan menu.


### 5. Debugging Error Program

Prompt yang digunakan:

```text
Program mengalami error. Bantu jelaskan penyebab error dan cara memperbaikinya.
```

Contoh error yang terjadi:

```text
NameError: name 'keyword' is not defined
```

Bantuan yang diberikan AI:

AI membantu menjelaskan bahwa error tersebut terjadi karena variabel `keyword` belum dibuat atau posisinya tidak sesuai sebelum digunakan dalam proses pencarian kandidat.

Solusi yang diterapkan:

Variabel `keyword` didefinisikan terlebih dahulu sebelum digunakan dalam perulangan linear search.

Contoh perbaikan:

```python
keyword = input("Masukkan nama kandidat yang dicari: ").strip().lower()

if not keyword:
    print("Keyword pencarian tidak boleh kosong!")
    return
```

Setelah itu, variabel `keyword` baru digunakan pada proses pencarian:

```python
for kandidat in kandidat_list:
    if keyword in kandidat["nama"].lower():
        hasil.append(kandidat)
```

Pelajaran yang didapat:

Saya memahami bahwa setiap variabel harus dibuat terlebih dahulu sebelum digunakan. Saya juga belajar membaca pesan error Python untuk mengetahui letak dan penyebab masalah.


## Refleksi Penggunaan AI

AI membantu dalam proses perancangan dan debugging proyek. Bantuan AI membuat proses pengerjaan menjadi lebih terarah, terutama saat menyusun struktur folder, desain top-down, pseudocode, dan sketsa tampilan console.

Namun, hasil dari AI tetap perlu diperiksa dan disesuaikan kembali. Tidak semua saran langsung digunakan begitu saja. Saya tetap perlu memahami alur program, mencoba menjalankan kode, membaca pesan error, dan memperbaiki bagian yang belum sesuai.

Dari proses ini, saya belajar bahwa AI dapat digunakan sebagai alat bantu belajar dan partner diskusi, tetapi pemahaman terhadap program tetap menjadi tanggung jawab pengembang.


## Kesimpulan

Penggunaan AI dalam proyek ini berperan sebagai pendukung dalam tahap perancangan dan debugging. AI membantu memberikan gambaran awal, tetapi implementasi akhir tetap perlu dipahami, diuji, dan disesuaikan agar sesuai dengan kebutuhan proyek Sistem Voting / E-Polling.

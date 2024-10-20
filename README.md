# Tugas-Lampu-Lalu-Lintas-Daspro
#### Nama: Rizky Yunia
#### Nim: 2409116089
#### Tugas Aplikasi Sederhana Lampu Lalu Lintas Jalan

#### Menggunakan time sebagai waktu dari lampu lalu lintas
import time
#### Membuat Function Untuk Lampu Lalu Lintas
#### Menggunakan range untuk menghitung mundur waktu
def lampu_lalulintas(arah_lampu):
    for i in range (10, 0, -1):
#### Sebagai output untuk menampilkan waktu yang menghitung mundur
        print(f"Lampu Merah {arah_lampu} - Berhenti selama {i} detik")
#### Sebagai jeda dari waktu yang sudah ditentukan sebelumnya       
        time.sleep(1)
#### Menggunakan range untuk menghitung mundur waktu
    for i in range (5, 0, -1):
#### Sebagai output untuk menampilkan waktu yang menghitung mundur
        print(f"Lampu Kuning {arah_lampu} - Bersiap-siap dalam {i} detik")
#### Sebagai jeda waktu yang sudah ditentukan sebelumnya
        time.sleep(1)
#### Menggunakan range untuk menghitung mundur waktu
    for i in range (20, 0, -1):
#### Sebagai output untuk menampilkan waktu menghitung mundur
        print(f"Lampu Hijau {arah_lampu} - Jalan {i} detik")
#### Sebagai jeda waktu yang ditentukan sebelumnya
        time.sleep(1)

#### Membuat Function Untuk Mendefinisikan Arah Lampu
def empat_arah():
    arah_lampu = ("Utara", "Timur", "Selatan", "Barat")

#### Melakukan Pengulangan Tanpa Henti Menggunakan while True:
while True:
        for arah in arah_lampu: 
            lampu_lalulintas(arah)

#### Memanggil Function Untuk Memulai Program
empat_arah()

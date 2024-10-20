import time

def lampu_lalulintas(arah_lampu):
    for i in range (10, 0, -1):
        print(f"Lampu Merah {arah_lampu} - Berhenti selama {i} detik")
        time.sleep(1)

    for i in range (5, 0, -1):
        print(f"Lampu Kuning {arah_lampu} - Bersiap-siap dalam {i} detik")
        time.sleep(1)

    for i in range (20, 0, -1):
        print(f"Lampu Hijau {arah_lampu} - Jalan {i} detik")
        time.sleep(1)

def empat_arah():
    arah_lampu = ("Utara", "Timur", "Selatan", "Barat")

    while True:
        for arah in arah_lampu:
            lampu_lalulintas(arah)

empat_arah()
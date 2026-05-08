import random
import time
from datetime import datetime, timedelta

def garis():
    print("=" * 60)

def garis_putus():
    print("-" * 60)

def main():
    garis()
    print("Selamat Datang di Sistem Pemesanan Tiket Pesawat XYZ")
    garis()

    # 1. Input Identitas Penumpang
    print("\n--- Data Penumpang ---")
    nama = input("Masukkan Nama Lengkap  : ").upper()
    ktp = input("Masukkan No. KTP/Paspor: ")
    no_hp = input("Masukkan No. HP        : ")

    # Data Mockup Rute & Harga Dasar
    rute_penerbangan = {
        "1": {"tujuan": "Jakarta (CGK) -> Bali (DPS)", "harga": 1200000},
        "2": {"tujuan": "Jakarta (CGK) -> Surabaya (SUB)", "harga": 950000},
        "3": {"tujuan": "Jakarta (CGK) -> Singapura (SIN)", "harga": 2500000},
        "4": {"tujuan": "Bali (DPS) -> Tokyo (NRT)", "harga": 7500000}
    }

    # 2. Pemilihan Rute
    print("\n--- Rute Penerbangan ---")
    for key, val in rute_penerbangan.items():
        print(f"[{key}] {val['tujuan']} - Rp {val['harga']:,}")
    
    pilih_rute = input("Pilih rute (1-4): ")
    while pilih_rute not in rute_penerbangan:
        print("Pilihan tidak valid!")
        pilih_rute = input("Pilih rute (1-4): ")
    
    rute_terpilih = rute_penerbangan[pilih_rute]

    # Data Mockup Maskapai
    maskapai_list = {
        "1": {"nama": "Garuda Indonesia", "multiplier": 1.5},
        "2": {"nama": "Citilink", "multiplier": 1.0},
        "3": {"nama": "AirAsia", "multiplier": 0.8},
        "4": {"nama": "Batik Air", "multiplier": 1.2}
    }

    # 3. Pemilihan Maskapai
    print("\n--- Pilih Maskapai ---")
    for key, val in maskapai_list.items():
        estimasi_harga = int(rute_terpilih['harga'] * val['multiplier'])
        print(f"[{key}] {val['nama']} (Estimasi: Rp {estimasi_harga:,})")
    
    pilih_maskapai = input("Pilih maskapai (1-4): ")
    while pilih_maskapai not in maskapai_list:
        print("Pilihan tidak valid!")
        pilih_maskapai = input("Pilih maskapai (1-4): ")
    
    maskapai_terpilih = maskapai_list[pilih_maskapai]
    total_harga = int(rute_terpilih['harga'] * maskapai_terpilih['multiplier'])

    # 4. Pemilihan Jadwal
    print("\n--- Pilih Jadwal Keberangkatan ---")
    besok = datetime.now() + timedelta(days=1)
    tanggal = besok.strftime("%d %B %Y")
    
    jadwal_list = [
        {"berangkat": "06:00", "tiba": "08:15"},
        {"berangkat": "13:30", "tiba": "15:45"},
        {"berangkat": "19:00", "tiba": "21:15"}
    ]
    
    print(f"Tanggal Penerbangan: {tanggal}")
    for i, jadwal in enumerate(jadwal_list, 1):
        print(f"[{i}] Berangkat: {jadwal['berangkat']} | Tiba: {jadwal['tiba']}")
        
    pilih_jadwal = input("Pilih jadwal (1-3): ")
    while pilih_jadwal not in ["1", "2", "3"]:
        print("Pilihan tidak valid!")
        pilih_jadwal = input("Pilih jadwal (1-3): ")
        
    jadwal_terpilih = jadwal_list[int(pilih_jadwal)-1]

    # 5. Pembayaran
    print("\n--- Pembayaran ---")
    print(f"Total yang harus dibayar: Rp {total_harga:,}")
    print("[1] Transfer Bank")
    print("[2] Kartu Kredit")
    print("[3] E-Wallet (Gopay/OVO/Dana)")
    
    pilih_bayar = input("Pilih metode pembayaran (1-3): ")
    while pilih_bayar not in ["1", "2", "3"]:
        print("Pilihan tidak valid!")
        pilih_bayar = input("Pilih metode pembayaran (1-3): ")
        
    print("\nMemproses pembayaran", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n\n✅ PEMBAYARAN BERHASIL!")
    time.sleep(1)

    # Generate Random Data for Boarding Pass
    booking_code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
    flight_number = maskapai_terpilih['nama'][:2].upper() + "-" + str(random.randint(100, 999))
    seat = str(random.randint(1, 30)) + random.choice(["A", "B", "C", "D", "E", "F"])
    gate = "G" + str(random.randint(1, 10))

    # 6. Cetak Boarding Pass
    print("\n\n" + "=" * 60)
    print("                    E-BOARDING PASS")
    print("=" * 60)
    print(f"MASKAPAI    : {maskapai_terpilih['nama']}")
    print(f"KODE BOOKING: {booking_code}               FLIGHT NO : {flight_number}")
    garis_putus()
    print(f"NAMA        : {nama}")
    print(f"RUTE        : {rute_terpilih['tujuan']}")
    print(f"TANGGAL     : {tanggal}")
    garis_putus()
    print(f"BERANGKAT   : {jadwal_terpilih['berangkat']}              GATE      : {gate}")
    print(f"TIBA        : {jadwal_terpilih['tiba']}              SEAT      : {seat}")
    garis_putus()
    print("STATUS      : PAID / CHECKED IN")
    print("=" * 60)
    print("Terima kasih telah terbang bersama kami. Semoga perjalanan Anda menyenangkan!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
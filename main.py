from datetime import datetime

saldo = 0
transaksi = []

def tambah_pemasukan():
    global saldo
    try:
        jumlah = input("Masukkan jumlah pemasukan: ")
        jumlah = float(jumlah)
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return
    keterangan = input("Keterangan (opsional): ").strip()
    saldo += jumlah
    transaksi.append({
        "type": "Pemasukan",
        "amount": jumlah,
        "keterangan": keterangan,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"Berhasil menambahkan pemasukan: Rp{jumlah:.2f}")
    print(f"Saldo sekarang: Rp{saldo:.2f}")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = input("Masukkan jumlah pengeluaran: ")
        jumlah = float(jumlah)
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return
    if jumlah > saldo:
        print("Saldo tidak cukup.")
        return
    keterangan = input("Keterangan (opsional): ").strip()
    saldo -= jumlah
    transaksi.append({
        "type": "Pengeluaran",
        "amount": jumlah,
        "keterangan": keterangan,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"Berhasil menambahkan pengeluaran: Rp{jumlah:.2f}")
    print(f"Saldo sekarang: Rp{saldo:.2f}")

def lihat_saldo():
    print(f"Saldo sekarang: Rp{saldo:.2f}")

def laporan():
    total_pemasukan = sum(t["amount"] for t in transaksi if t["type"] == "Pemasukan")
    total_pengeluaran = sum(t["amount"] for t in transaksi if t["type"] == "Pengeluaran")
    print("=== Laporan Rekap Uang Saku ===")
    print(f"Total pemasukan   : Rp{total_pemasukan:.2f}")
    print(f"Total pengeluaran : Rp{total_pengeluaran:.2f}")
    print(f"Saldo sekarang     : Rp{saldo:.2f}")
    print("\nRiwayat transaksi:")
    if not transaksi:
        print("Belum ada transaksi.")
        return
    for i, t in enumerate(transaksi, start=1):
        keterangan = t["keterangan"] if t["keterangan"] else "-"
        print(f"{i}. [{t['waktu']}] {t['type']}: Rp{t['amount']:.2f} - {keterangan}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")
    print("5. Laporan")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "5":
        laporan()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
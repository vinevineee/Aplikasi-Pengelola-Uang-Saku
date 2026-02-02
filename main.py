saldo = 0

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
    saldo += jumlah
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
    saldo -= jumlah
    print(f"Berhasil menambahkan pengeluaran: Rp{jumlah:.2f}")
    print(f"Saldo sekarang: Rp{saldo:.2f}")

def lihat_saldo():
    print(f"Saldo sekarang: Rp{saldo:.2f}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
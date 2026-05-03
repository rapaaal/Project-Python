saldo = 10000000000
pin = 1234
print("========SELAMAT DATANG=========")
input_pin = input("PIN : ")

if(input_pin == pin):
    while True:
        print("Menu")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Keluar")
        pilihan = int(input("Pilih : "))

        if pilihan == 1 :
            print(f"Rp. {saldo:,}")
        elif pilihan == 2 :
            setor = int(input("Jumlah Setor : "))
            if(setor > 0):
                saldo += setor
                print("Berhasil. Saldo Anda Rp. {saldo}")
        elif pilihan == 3 :
            tarik = int(input("Jumlah Tarik : "))
            if (tarik > 0):
                saldo -= tarik
                print(f"Berhasil. Saldo Anda Rp. {saldo:,}")
        elif pilihan == 4 :
            print("Terima Kasih")
            break
else:
    print("PIN Anda Salah!")
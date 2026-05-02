print("=========WARMINDO========")
pembeli = input("Nama Pembeli :")
print("Nama Pembeli :")

def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n===========MENU WARMINDO===========")
    print("1. Mie Bangladesh - Rp.20000,00")
    print("2. Mie Bangladesh spesial - Rp.25000,00")
    print("3. Indomie Goreng/kuah - Rp.10000,00")
    print("4. Nasi kucing - Rp.5000,00")
    print("5. Nasi bakar - Rp.6000,00")
    nomor = int(input("Masukkan Pilihn 1/2/3/4/5 : "))
    porsi = int(input("Jumlah porsi : "))

    if nomor == 1:
        totalmakanan = porsi * 20000
        print(porsi, "Mie Bangladesh = Rp.",totalmakanan)
        makan = ("Mie Bangladesh")
    elif nomor == 2:
        totalmakanan = porsi * 25000
        print(porsi, "Mie Bangladesh spesial = Rp.",totalmakanan)
        makan = ("Mie Bangladesh spesial")
    elif nomor == 3:
        totalmakanan = porsi * 10000
        print(porsi, "Indomie goreng/kuah = Rp.",totalmakanan)
        makan = ("Indomie goreng/kuah")
    elif nomor == 4:
        totalmakanan = porsi * 5000
        print(porsi, "Nasi kucing = Rp.",totalmakanan)
        makan = ("Nasi kucing")
    elif nomor == 5:
        totalmakanan = porsi * 6000
        print(porsi, "Nasi bakar = Rp.",totalmakanan)
        makan = ("Nasi bakar")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !")
        makanan()
def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n===========MENU WARMINDO===========")
    print("1. Es teh - Rp.4000,00")
    print("2. Es jeruk - Rp.5000,00")
    print("3. Kopi - Rp.5000,00")
    print("4. Nutrisari - Rp.5000,00")
    print("5. Es susu - Rp.5000,00")
    nomor = int(input("Masukkan Pilihn 1/2/3/4/5 : "))
    gelas = int(input("Jumlah gelas : "))

    if nomor == 1:
        totalminuman = gelas *4000
        print(gelas, "Es teh = Rp.",totalminuman)
        minum = ("Es teh")
    elif nomor == 2:
        totalminuman = gelas * 5000
        print(gelas, "Es jeruk = Rp.",totalminuman)
        minum = ("Es jeruk")
    elif nomor == 3:
        totalminuman = gelas * 5000
        print(gelas, "Kopi = Rp.",totalminuman)
        minum = ("Kopi")
    elif nomor == 4:
        totalminuman = gelas * 5000
        print(gelas, "Nutrisari = Rp.",totalminuman)
        minum = ("Nutrisari")
    elif nomor == 5:
        totalminuman = gelas * 5000
        print(gelas, "Es susu = Rp.",totalminuman)
        minum = ("Es susu")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !")
        minuman()

makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\n Total yang harus di bayar : ",total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = int(uang - total_semua)
print("Kembalian : ", kembalian)

print("\n=============S T R U K B E L I ===============")
print("Nama\t\t: ",pembeli)
print("Nama\t\t: ",porsi,makan, "(Rp.", totalmakanan,")")
print("Nama\t\t: ",gelas,minum, "(Rp.", totalminuman,")")
print("Tagihan\t\t: ",total_semua)
print("Dibayar\t\t: ",uang)
print("kembalian\t: ",kembalian)

print("=========================================")
print("=========================================")
data_product = {
    1:"Laptop",
    2:"Monitor",
    3:"Mouse ",
    4:"Mouse Pad",
    5:"Charger"
}
daftar_harga = {
    1: 60000000,
    2: 8000000,
    3: 200000,
    4: 70000,
    5: 500000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash on Delivery",
    4:"Kartu Kredit"
}
print("====================List Product===================")
for i in data_product :
    print("Id Product : ", i, "\t Nama Product : ", data_product[i], "\t Harga Product : ", daftar_harga[i])
pilih_id = int(input("Pilih Id Product : "))
if pilih_id in data_product :
    pilih_beli = input("Ingin Beli > (Y/N) : ")
    if pilih_beli == "y" or pilih_beli == "Y" :
        nama_penerima    = input("Nama Penerima    : ")
        alamat_penerima  = input("Alamat Penerima  : ")
        telepon          = input("No HP            : ")
        kurir_pengiriman = input("Kurir Pengiriman : ")
        dict_trx = {
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "No HP":telepon,
            "kurir Pengiriman":kurir_pengiriman,
            "product id":data_product,
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("======================== Metode Pembayaran =================================")
    for i in daftar_metode_pembayaran :
        print("id : ", i, "\t Metode Pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih Id Metode Pembayaran : "))
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima : ", dict_trx["nama penerima"])
        print("Alamat Penerima : ", dict_trx["alamat penerima"])
        print("No HP : ", dict_trx["nama penerima"])
        print("Kurir Pengiriman : ", dict_trx["kurir Pengiriman"])
        print("Product : ", data_product[pilih_id])
        print("Harga : ", daftar_harga[pilih_id])
        print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah Anda Yakin ingin Melakukan Pembayaran? (Y/N) : ")
        if konfirmasi == "y" or konfirmasi == "Y":
            print("Anda Sudah berhasil melakukan pembayaran")
        else:
            pass
    else:
        print("Id metode pembayaran tidak tersedia")
else:
    print("id Product tidak tersedia")

    
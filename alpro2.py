#header 
print("=" *40)
print("         KANTIN POLINES DIGITAL")
print("             Sistem Kasir V1")
print("=" *40)

#input data transaksi
Nama_Barang = input("Nama Barang : ")
Harga_satuan = int(input("Harga Satuan : Rp "))
Jumlah_Barang = int(input("Jumlah : "))
Total_Harga = Harga_satuan * Jumlah_Barang

#print total harga 
print(f"Total Harga = {Total_Harga}")

#Uang bayar
Uang_Bayar = int(input("Masukan Uang Bayar : Rp "))

#output struk transaksi
if Uang_Bayar >= Total_Harga:
    kembalian = Uang_Bayar - Total_Harga
    print("\n" + "=" *40)
    print("             STRUK BELANJA")
    print("=" *40)
    print(f"Nama Barang :  {Nama_Barang}")
    print(f"Harga Barang : {Harga_satuan}")
    print(f"Jumlah Beli : {Jumlah_Barang}")
    print("-" *40)
    print(f"Total Harga : Rp {Total_Harga}")
    print(f"Uang Bayar : Rp {Uang_Bayar}" )
    print(f"Kembalian : Rp {kembalian}")
    print("=" *40)
    print("             Terima Kasih")
    print("            Kantin Polines")
    print("=" *40)

else: 
    Kekurangan = Total_Harga - Uang_Bayar
    print("\nUang Pembayaran Tidak Mencukupi!")
    print(f"Kekuarangan uang : Rp {Kekurangan}")
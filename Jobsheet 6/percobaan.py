# Program Penyimpanan Data Mahasiswa
print("=== DATABASE MAHASISWA INFORMATIKA ===")


# List yang berisi kumpulan Dictionary
database_mhs = [
    {"nim": "26001", "nama": "Ahmad", "prodi": "Informatika"},
    {"nim": "26002", "nama": "Siti", "prodi": "Informatika"},
    {"nim": "26003", "nama": "Budi", "prodi": "Sistem Informasi"}
]


# Menambah dictionary baru ke dalam list
mhs_baru = {"nim": "26004", "nama": "Citra", "prodi": "Informatika"}
database_mhs.append(mhs_baru)


# Menampilkan data dengan perulangan


print(f"{'NIM':<10} | {'NAMA':<10} | {'PRODI'}")


for mhs in database_mhs:
    print(f"{mhs['nim']:<10} | {mhs['nama']:<10} | {mhs['prodi']}")

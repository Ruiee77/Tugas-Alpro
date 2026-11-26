
daftar_hadir = []

while True:
    print("\n=== MENU PRESENSI KULIAH ===")
    print("1. Tambah Hadir")
    print("2. Hapus Presensi")
    print("3. Lihat & Urutkan")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ").strip()

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ").strip()
        if nama == "":
            print("Nama tidak boleh kosong!")
        else:
            daftar_hadir.append(nama)
            print(f"{nama} berhasil ditambahkan ke daftar hadir.")

    elif pilihan == "2":
        nama = input("Masukkan nama yang akan dihapus: ").strip()
        if nama in daftar_hadir:
            daftar_hadir.remove(nama)
            print(f"{nama} berhasil dihapus dari daftar hadir.")
        else:
            print(f"{nama} tidak ditemukan dalam daftar hadir.")

    elif pilihan == "3":
        if len(daftar_hadir) == 0:
            print("Daftar hadir masih kosong.")
        else:
            terurut = sorted(daftar_hadir)
            print("\nDaftar Hadir (urut alfabetis):")
            for i, nama in enumerate(terurut, start=1):
                print(f"{i}. {nama}")
            print(f"Total hadir: {len(terurut)} mahasiswa")

    elif pilihan == "4":
        print("Terima kasih. Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Masukkan angka 1-4.")
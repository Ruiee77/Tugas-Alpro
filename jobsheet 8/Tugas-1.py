"""Studi Kasus 1: Aplikasi ATM Mini Modular (Menu-Driven Functions)."""

MIN_TARIK = 50_000


def format_rupiah(angka):
    """Format angka menjadi 'Rp 1.500.000' (pemisah ribuan titik)."""
    return "Rp {:,.0f}".format(angka).replace(",", ".")


def cek_saldo(saldo):
    """Menampilkan saldo terkini dalam format Rupiah."""
    print(f"Saldo Anda saat ini: {format_rupiah(saldo)}")


def setor_tunai(saldo, nominal):
    """Validasi nominal > 0, tambahkan ke saldo, kembalikan saldo terbaru."""
    if nominal <= 0:
        print("Setor gagal: nominal harus lebih dari Rp 0.")
        return saldo
    saldo += nominal
    print(f"Setor tunai {format_rupiah(nominal)} berhasil.")
    return saldo


def tarik_tunai(saldo, nominal):
    """Validasi minimal penarikan Rp 50.000 dan kecukupan saldo,
    lalu kembalikan saldo terbaru."""
    if nominal < MIN_TARIK:
        print(f"Tarik gagal: minimal penarikan {format_rupiah(MIN_TARIK)}.")
        return saldo
    if nominal > saldo:
        print("Tarik gagal: saldo tidak mencukupi.")
        return saldo
    saldo -= nominal
    print(f"Tarik tunai {format_rupiah(nominal)} berhasil.")
    return saldo


def baca_nominal(prompt):
    """Membaca input angka; mengembalikan None jika input tidak valid."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Input tidak valid, masukkan angka bulat.")
        return None


def tampilkan_menu():
    print("\n===== ATM MINI KAMPUS =====")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Keluar")


def main():
    saldo = 1_000_000  # saldo awal prototipe
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            cek_saldo(saldo)
        elif pilihan == "2":
            nominal = baca_nominal("Nominal setor: Rp ")
            if nominal is not None:
                saldo = setor_tunai(saldo, nominal)
        elif pilihan == "3":
            nominal = baca_nominal("Nominal tarik: Rp ")
            if nominal is not None:
                saldo = tarik_tunai(saldo, nominal)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan ATM Mini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak tersedia, coba lagi.")


if __name__ == "__main__":
    main()

"""Sistem E-Parking Terpadu - Polines. Data disimpan di eparking_data.txt"""

import os
import sys
from datetime import datetime

FILE_DATA = "eparking_data.txt"
TARIF_DASAR = {1: 3000, 2: 6000}    # 2 jam pertama
TARIF_PER_JAM = {1: 1000, 2: 2000}  # jam ke-3 dst
NAMA_JENIS = {1: "Motor", 2: "Mobil"}
KOLOM = ["waktu", "petugas", "plat", "jenis", "durasi", "member",
         "biaya_parkir", "denda", "diskon", "total", "bayar", "kembalian"]
KOLOM_ANGKA = ["durasi", "biaya_parkir", "denda", "diskon", "total", "bayar", "kembalian"]


# ---------- Utilitas ----------
def rupiah(angka):
    return "Rp " + f"{int(angka):,}".replace(",", ".")


def waktu_sekarang():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def garis(char="=", n=50):
    print(char * n)


def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Error: Input harus berupa angka!")


def bersihkan(teks):
    """Hapus tanda '|' agar tidak merusak format file txt."""
    return teks.replace("|", "").strip()


# ---------- Penyimpanan data (file txt) ----------
def muat_data():
    data = {"akun": {}, "riwayat": []}
    if os.path.exists(FILE_DATA):
        for baris in open(FILE_DATA, encoding="utf-8"):
            k = baris.strip().split("|")
            if k[0] == "AKUN":
                data["akun"][k[1]] = dict(zip(["nama", "nim", "password", "tgl_daftar"], k[2:]))
            elif k[0] == "RIWAYAT":
                trx = dict(zip(KOLOM, k[1:]))
                for key in KOLOM_ANGKA:
                    trx[key] = int(trx[key])
                data["riwayat"].append(trx)
    return data


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        for username, a in data["akun"].items():
            f.write("|".join(["AKUN", username, a["nama"], a["nim"],
                              a["password"], a["tgl_daftar"]]) + "\n")
        for t in data["riwayat"]:
            f.write("|".join(["RIWAYAT"] + [str(t[k]) for k in KOLOM]) + "\n")


# ---------- TAHAP 1: Registrasi ----------
def buat_username(nama):
    return nama.lower().replace(" ", "")


def buat_password(nim):
    return "parkir" + nim[-3:]


def registrasi(data):
    garis()
    print("REGISTRASI AKUN PETUGAS JAGA")
    garis()
    nama = bersihkan(input("Nama Lengkap Mahasiswa : "))
    nim = input("NIM (tanpa titik)      : ").strip()
    if not nama or not nim.isdigit() or len(nim) < 3:
        print("Error: Nama wajib diisi dan NIM harus angka minimal 3 digit!")
        return

    username = buat_username(nama)
    if username in data["akun"]:
        print("Error: Akun dengan username tersebut sudah terdaftar!")
        return

    data["akun"][username] = {"nama": nama, "nim": nim,
                              "password": buat_password(nim),
                              "tgl_daftar": waktu_sekarang()}
    simpan_data(data)
    print(f"\nRegistrasi berhasil!\nUsername : {username}\nPassword : {buat_password(nim)}")


# ---------- TAHAP 2: Login ----------
def login(data):
    garis()
    print("LOGIN PETUGAS")
    garis()
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    if username not in data["akun"]:
        print("Error: Username petugas tidak terdaftar!")
        sys.exit()
    akun = data["akun"][username]
    if password != akun["password"]:
        print("Error: Password salah! Akses ditolak.")
        sys.exit()

    print(f"Login Berhasil! Selamat Bertugas, {akun['nama']}.")
    return akun


# ---------- TAHAP 3: Perhitungan ----------
def hitung_biaya_parkir(jenis, durasi):
    return TARIF_DASAR[jenis] + max(durasi - 2, 0) * TARIF_PER_JAM[jenis]


def hitung_denda(durasi):
    return 20000 if durasi > 12 else 0


def hitung_diskon(biaya_parkir, member):
    return int(biaya_parkir * 0.30) if member == "ya" else 0


def hitung_total(biaya_parkir, denda, diskon):
    return biaya_parkir + denda - diskon


def proses_pembayaran(total):
    """Ulangi input sampai uang mencukupi. Mengembalikan (bayar, kembalian)."""
    while True:
        bayar = input_angka("Nominal Uang Bayar : Rp ")
        if bayar >= total:
            return bayar, bayar - total
        print("Transaksi GAGAL! Uang pembayaran kurang.")
        print(f"  Kekurangan : {rupiah(total - bayar)}")
        print("Silakan masukkan kembali nominal pembayaran.\n")


def cetak_struk(trx):
    garis()
    print("        STRUK PEMBAYARAN RESMI E-PARKING")
    print("          POLITEKNIK NEGERI SEMARANG")
    garis()
    print(f"Tanggal/Waktu   : {trx['waktu']}")
    print(f"Petugas         : {trx['petugas']}")
    print(f"No. Polisi      : {trx['plat']}")
    print(f"Jenis Kendaraan : {trx['jenis']}")
    print(f"Durasi Parkir   : {trx['durasi']} jam")
    print(f"Stiker Member   : {trx['member']}")
    garis("-")
    print(f"Biaya Parkir    : {rupiah(trx['biaya_parkir'])}")
    print(f"Denda Inap      : {rupiah(trx['denda'])}")
    print(f"Diskon Member   : -{rupiah(trx['diskon'])}")
    garis("-")
    print(f"TOTAL TAGIHAN   : {rupiah(trx['total'])}")
    print(f"Uang Bayar      : {rupiah(trx['bayar'])}")
    print(f"Kembalian       : {rupiah(trx['kembalian'])}")
    garis()
    print("   Status: LUNAS - Terima kasih & hati-hati!")
    garis()


def transaksi_parkir(data, akun):
    garis()
    print("TRANSAKSI PARKIR BARU")
    garis()
    plat = bersihkan(input("Nomor Polisi / Plat Kendaraan  : ")).upper()
    jenis = input_angka("Jenis Kendaraan (1=Motor, 2=Mobil): ")
    if jenis not in NAMA_JENIS:
        print("Error: Jenis kendaraan tidak valid!")
        sys.exit()
    durasi = input_angka("Durasi Parkir (jam)             : ")
    if durasi <= 0:
        print("Error: Durasi parkir harus lebih dari 0 jam!")
        return
    member = ""
    while member not in ("ya", "tidak"):
        member = input("Stiker Member Kampus (Ya/Tidak)  : ").strip().lower()

    biaya = hitung_biaya_parkir(jenis, durasi)
    denda = hitung_denda(durasi)
    diskon = hitung_diskon(biaya, member)
    total = hitung_total(biaya, denda, diskon)

    print(f"\nTotal Tagihan: {rupiah(total)}")
    bayar, kembalian = proses_pembayaran(total)

    trx = {"waktu": waktu_sekarang(), "petugas": akun["nama"], "plat": plat,
           "jenis": NAMA_JENIS[jenis], "durasi": durasi, "member": member.capitalize(),
           "biaya_parkir": biaya, "denda": denda, "diskon": diskon,
           "total": total, "bayar": bayar, "kembalian": kembalian}
    data["riwayat"].append(trx)
    simpan_data(data)
    print()
    cetak_struk(trx)


# ---------- Riwayat ----------
def tampil_riwayat(data):
    garis()
    print("RIWAYAT TRANSAKSI PARKIR")
    garis()
    if not data["riwayat"]:
        print("Belum ada riwayat transaksi.")
        return
    print(f"{'No':<3} {'Waktu':<20} {'Plat':<11} {'Jenis':<6} {'Jam':<4} {'Total':>11}  Petugas")
    garis("-", 75)
    for i, t in enumerate(data["riwayat"], start=1):
        print(f"{i:<3} {t['waktu']:<20} {t['plat']:<11} {t['jenis']:<6} "
              f"{t['durasi']:<4} {rupiah(t['total']):>11}  {t['petugas']}")
    garis("-", 75)
    print(f"Jumlah transaksi : {len(data['riwayat'])}")
    print(f"Total pendapatan : {rupiah(sum(t['total'] for t in data['riwayat']))}")


# ---------- Menu ----------
def menu_petugas(data, akun):
    while True:
        print()
        garis()
        print(f"MENU PETUGAS - {akun['nama']}")
        print(f"Tanggal: {waktu_sekarang()}")
        garis()
        print("1. Transaksi Parkir Baru\n2. Lihat Riwayat Parkir\n3. Logout")
        pilihan = input("Pilih menu [1-3]: ").strip()
        if pilihan == "1":
            transaksi_parkir(data, akun)
        elif pilihan == "2":
            tampil_riwayat(data)
        elif pilihan == "3":
            print("Logout berhasil.")
            return
        else:
            print("Pilihan tidak valid!")


def menu_utama():
    data = muat_data()
    while True:
        print()
        garis()
        print("   SISTEM E-PARKING TERPADU - POLINES")
        print(f"   Tanggal: {datetime.now().strftime('%A, %d-%m-%Y')}")
        garis()
        print("1. Registrasi Akun Petugas\n2. Login\n3. Keluar")
        pilihan = input("Pilih menu [1-3]: ").strip()
        if pilihan == "1":
            registrasi(data)
        elif pilihan == "2":
            menu_petugas(data, login(data))
        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_utama()
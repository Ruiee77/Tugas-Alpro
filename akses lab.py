
# Fungsi untuk meminta input sampai jawabannya valid
def minta_pilihan(pesan, pilihan):
    while True:
        jawaban = input(pesan)
        jawaban = jawaban.strip()   # hapus spasi di awal/akhir
        jawaban = jawaban.lower()   # ubah jadi huruf kecil
 
        if jawaban in pilihan:
            return jawaban
 
        print("Input tidak valid, silakan coba lagi.")
 
 
# Program utama
print("=== Sistem Akses Laboratorium Komputer ===")
 
status_mahasiswa = minta_pilihan("Status Mahasiswa (Aktif / Non-Aktif): ", ["aktif", "non-aktif"])
 
if status_mahasiswa == "aktif":
    status_ukt = minta_pilihan("Status UKT (Lunas / Tunggakan): ", ["lunas", "tunggakan"])
 
    if status_ukt == "lunas":
        print("Akses diterima: Silakan masuk ke Laboratorium Komputer")
    else:
        print("Akses ditolak: Silakan selesaikan pembayaran UKT")
else:
    print("Akses ditolak: Mahasiswa tidak aktif")

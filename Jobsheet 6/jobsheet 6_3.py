PIN_BENAR = "1234"
MAKS_PERCOBAAN = 3

print("=" * 40)
print("      PORTAL AKADEMIK - LOGIN AMAN")
print("=" * 40)

percobaan = 0
berhasil = False

while percobaan < MAKS_PERCOBAAN:
    pin = input(f"Masukkan PIN (percobaan {percobaan + 1}/{MAKS_PERCOBAAN}): ")
    percobaan += 1

    if pin == PIN_BENAR:
        berhasil = True
        break

    sisa = MAKS_PERCOBAAN - percobaan
    if sisa > 0:
        print(f"PIN salah! Sisa kesempatan: {sisa}\n")

print()
if berhasil:
    print("Login Berhasil")
    print("Selamat datang di Portal Akademik!")
else:
    print("ERROR: Kesempatan habis (3 kali salah).")
    print("Akun dikunci. Sistem keluar.")
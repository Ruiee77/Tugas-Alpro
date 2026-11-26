
print("=" * 36)
print("   PENCETAK POLA SEGITIGA BINTANG")
print("=" * 36)

while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
        if baris > 0:
            break
        print("[!] Jumlah baris harus lebih dari 0.\n")
    except ValueError:
        print("[!] Input harus berupa angka bulat.\n")

# Pola utama: segitiga siku-siku (nested loop)
print("\nPola 1 - Segitiga Siku-siku:")
for i in range(1, baris + 1):          # loop luar: baris
    for j in range(i):                 # loop dalam: bintang per baris
        print("*", end="")
    print()
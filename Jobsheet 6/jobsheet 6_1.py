
print("=" * 44)
print("   KALKULATOR FAKTORIAL (perulangan while)")
print("=" * 44)

while True:
    try:
        n = int(input("Masukkan angka bulat positif: "))
        if n >= 0:
            break
        print("[!] Angka harus positif. Coba lagi.\n")
    except ValueError:
        print("[!] Input harus berupa angka bulat. Coba lagi.\n")

# Hitung faktorial dengan while
hasil = 1
i = n
langkah = []
while i >= 1:
    hasil *= i
    langkah.append(str(i))
    i -= 1

rumus = " x ".join(langkah) if langkah else "1"
print()
print(f"{n}! = {rumus} = {hasil}")
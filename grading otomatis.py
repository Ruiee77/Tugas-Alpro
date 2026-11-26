

print("=== Grading Akademik ===")

def main():
    #input nilai
    mahasiswa = input("Masukan Nama Mahasiswa : ")
    nilai = int(input("Masukan Nilai (0-100): "))

    if nilai < 0 or nilai > 100:
        print("Error, nilai tidak valid")
        return nilai
    elif nilai >= 85 :
        Grade = "A"
        Status = "LULUS"
        Pesan = "Nice Work, Pertahankan"
    elif nilai >= 75 :
        Grade = "B"
        Status = "LULUS"
        Pesan = "Good job, Tingkatkan lagi"
    elif nilai >= 65 :
        Grade = "C"
        Status = "Remidial"
        Pesan = "Silahkan Mengikuti Remidial"
    elif nilai >= 50 :
        Grade = "D"
        Status = "Remidial"
        Pesan = "Silahkan Mengikuti Remidial"
    else :
        Grade = "E"
        Status = "Remidial"
        Pesan = "Silahkan Mengikuti Remidial"

    print("-" *30)
    print(f"Nama : {mahasiswa}") 
    print(f"Nilai : {nilai}")
    print(f"Grade : {Grade}")
    print(f"Status : {Status}")
    print(f"Pesan : {Pesan}")
    print("-" *30)

while True :
    main()

    while True:

        ulang = input("Apakah anda ingin menginput nilai lain (y/n) : ").lower()
        if ulang in ['y', 'n']:
            break
        print("Input tidak valid, masukan 'y' untuk Ya dan 'n' untuk tidak.\n")

    if ulang != 'y':
        print("Selesai, Terima Kasih!")
        break
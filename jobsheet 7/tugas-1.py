nilai_ujian = [78, 85 ,90, 65, 88, 72, 95, 80]

nilai_ujian.sort()
jmlh_mhsw = len(nilai_ujian)
nilai_tertinggi = max(nilai_ujian)
nilai_terendah = min(nilai_ujian)
rata_rata = sum(nilai_ujian) / jmlh_mhsw

print("=" * 20)
print("Pengolahan Daftar Nilai")
print("=" * 20)

print("Jumlah Mahasiswa : ", jmlh_mhsw)
print("Nilai tertinggi : ", nilai_tertinggi)
print("Nilai terendah : ", nilai_terendah)
print(f"Rata-rata :  {rata_rata:.2f}")

# Fungsi untuk menghitung rata-rata nilai.
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi untuk mengambil nilai yang lulus.
def nilai_lulus(data, batas=60):
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


# Input: Menyiapkan 10 nilai mahasiswa.
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Proses: Menghitung statistik dan kelulusan.
banyak_data = len(nilai)
total = sum(nilai)
minimum = min(nilai)
maksimum = max(nilai)
rata = rata_rata(nilai)

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# Output: Menampilkan ringkasan hasil.
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai       : {nilai}")
print(f"Banyak data         : {banyak_data}")
print(f"Total nilai         : {total}")
print(f"Rata-rata           : {rata:.2f}")
print(f"Nilai minimum       : {minimum}")
print(f"Nilai maksimum      : {maksimum}")
print(f"Batas kelulusan     : 60")
print(f"Nilai mahasiswa lulus: {lulus}")
print(f"Jumlah lulus        : {jumlah_lulus}")
print(f"Jumlah belum lulus  : {jumlah_belum_lulus}")

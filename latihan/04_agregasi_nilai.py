
# Input: Menyimpan lima nilai ke dalam list.
nilai = [75, 80, 65, 90, 88]

# Proses: Menghitung total, rata-rata,
# nilai minimum, dan nilai maksimum.
total = sum(nilai)
rata_rata = sum(nilai) / len(nilai)

# Output: Menampilkan hasil perhitungan.
print(f"Total = {total}")
print(f"Rata-rata = {rata_rata:.2f}")
print(f"Minimum = {min(nilai)}")
print(f"Maksimum = {max(nilai)}")

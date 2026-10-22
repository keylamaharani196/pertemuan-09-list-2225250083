
# Input: List nilai dan batas kelulusan 60.
nilai = [75, 55, 80, 60, 45, 90]
batas_lulus = 60

# Proses: Memeriksa setiap nilai.
# Nilai yang >= 60 dimasukkan ke list lulus.
lulus = []
for x in nilai:
    if x >= batas_lulus:
        lulus.append(x)

# Output: Menampilkan nilai yang lulus dan jumlahnya.
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")

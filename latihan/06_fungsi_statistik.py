
# Input: Menerima list nilai untuk dihitung rata-ratanya.
def rata_rata(data):
    # Proses: Jika list kosong, kembalikan nilai 0.
    if len(data) == 0:
        return 0

    # Menghitung total nilai dibagi banyak data.
    return sum(data) / len(data)


# Output: Menampilkan rata-rata nilai.
nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata = {rata_rata(nilai):.2f}")

# Pengujian tambahan untuk list kosong.
print(f"Rata-rata list kosong = {rata_rata([]):.2f}")

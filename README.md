# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Keyla Maharani  
**NIM:** 2225250083  
**Kelas:** 3E

## 1. Tujuan

Tujuan kegiatan ini adalah memahami penggunaan list Python untuk menyimpan, mengakses, mengubah, dan mengolah kumpulan data numerik. Selain itu, kegiatan ini melatih penggunaan indeks, slicing, fungsi agregasi, perulangan, dan fungsi untuk menganalisis data.

## 2. Struktur Program

Program pada Pertemuan 09 terdiri dari beberapa file latihan dan satu file praktik utama.

### A. Latihan

1. `latihan/01_buat_list.py`  
   Membuat dan menampilkan list dalam Python.

2. `latihan/02_indeks_slicing.py`  
   Mengakses elemen list menggunakan indeks dan mengambil bagian list menggunakan slicing.

3. `latihan/03_manipulasi_list.py`  
   Melakukan manipulasi list, seperti menambahkan dan mengubah elemen.

4. `latihan/04_agregasi_nilai.py`  
   Mengolah data numerik menggunakan fungsi agregasi, seperti `sum()`, `min()`, dan `max()`.

5. `latihan/05_filter_kelulusan.py`  
   Menyeleksi nilai berdasarkan batas kelulusan.

6. `latihan/06_fungsi_statistik.py`  
   Menggunakan fungsi untuk menghitung statistik sederhana dari kumpulan data.

### B. Praktik

`praktik/analisis_nilai_mahasiswa.py`

Program ini menganalisis 10 nilai mahasiswa menggunakan list. Hasil yang dihitung meliputi banyak data, total nilai, rata-rata, nilai minimum, nilai maksimum, daftar nilai lulus, jumlah mahasiswa lulus, dan jumlah mahasiswa belum lulus.

## 3. Cara Menjalankan

1. Buka folder proyek Pertemuan 09 di Visual Studio Code.
2. Buka terminal melalui menu **Terminal → New Terminal**.
3. Jalankan perintah berikut:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

Jika perintah `python3` tidak dapat digunakan di Windows, gunakan:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

4. Tekan Enter untuk menjalankan program.
5. Amati hasil analisis nilai yang ditampilkan pada terminal.

## 4. Test Case

**Data pengujian:**

```python
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
```

| No. | Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Menghitung banyak data | 10 | 10 | Berhasil |
| 2 | Menghitung total nilai | 695 | 695 | Berhasil |
| 3 | Menghitung rata-rata | 69.50 | 69.50 | Berhasil |
| 4 | Mencari nilai minimum | 45 | 45 | Berhasil |
| 5 | Mencari nilai maksimum | 90 | 90 | Berhasil |
| 6 | Menyeleksi nilai lulus dengan batas 60 | `[78, 90, 67, 60, 82, 71, 88]` | `[78, 90, 67, 60, 82, 71, 88]` | Berhasil |
| 7 | Menghitung jumlah mahasiswa lulus | 7 | 7 | Berhasil |
| 8 | Menghitung jumlah mahasiswa belum lulus | 3 | 3 | Berhasil |

**Kesimpulan pengujian:** Seluruh hasil aktual sesuai dengan hasil yang diharapkan. Program berhasil mengolah data nilai mahasiswa menggunakan list Python.

## 5. Refleksi

Melalui kegiatan ini, saya memahami bahwa list dapat digunakan untuk menyimpan banyak data dalam satu variabel sehingga data lebih mudah diakses dan diolah. Saya juga memahami penggunaan indeks, slicing, serta fungsi `len()`, `sum()`, `min()`, dan `max()` untuk mengolah data numerik.

Saya belajar bahwa batas kelulusan harus diperhatikan dengan benar. Pada program ini, nilai 60 termasuk lulus karena kondisi yang digunakan adalah `nilai >= 60`. Saya juga memahami pentingnya memeriksa list kosong sebelum menghitung rata-rata agar tidak terjadi kesalahan pembagian dengan nol.

## 6. Kesimpulan

List Python memudahkan penyimpanan dan pengolahan kumpulan data numerik. Dengan memanfaatkan fungsi bawaan dan fungsi buatan sendiri, program dapat menghitung statistik nilai mahasiswa serta mengelompokkan nilai berdasarkan batas kelulusan secara terstruktur.

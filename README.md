# Pertemuan 06 Nested Loop Python

Nama  : Hikmah Azizah

NIM   : 2225250086

Kelas : 3B  

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
* **Loop Luar (`for i in range(1, n + 1)`):** Mengatur iterasi baris (1 sampai n) serta mereset akumulator `total_baris` di setiap awal baris baru.
* **Loop Dalam (`for j in range(1, n + 1)`):** Mengatur iterasi kolom (1 sampai n) untuk memproses setiap sel (i, j) pada baris yang sedang berjalan.
* **Akumulator:**
  * `total_baris`: Menjumlahkan nilai hasil perkalian (i * j) khusus untuk baris i.
  * `total_semua`: Menjumlahkan seluruh hasil perkalian dari seluruh sel matriks n x n.
* **Counter:**
  * `count_genap`: Mencacah berapa kali hasil perkalian (i * j) menghasilkan bilangan genap (`hasil % 2 == 0`).

## Hasil Pengujian

| Input n | Hasil yang Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- |
| -1, lalu 2 | Meminta ulang input hingga n > 0, lalu mencetak tabel 2x2, Total = 9, Genap = 3 | Meminta ulang input hingga n > 0, mencetak tabel 2x2, Total = 9, Genap = 3 | Sesuai |
| 1 | Tabel 1x1, Jumlah baris 1 = 1, Total = 1, Genap = 0 | Tabel 1x1, Jumlah baris 1 = 1, Total = 1, Genap = 0 | Sesuai |
| 2 | Tabel 2x2, Total = 9, Genap = 3 | Tabel 2x2, Total = 9, Genap = 3 | Sesuai |
| 3 | Tabel 3x3, Total = 36, Genap = 5 | Tabel 3x3, Total = 36, Genap = 5 | Sesuai |

## Analisis Efisiensi
Badan loop dalam berjalan sebanyak n * n = n^2 kali untuk input n. Hal ini menunjukkan bahwa tingkat pertumbuhan kompleksitas waktu program ini adalah kuadratik O(n^2).

## Refleksi
* **Kesalahan Nested Loop:** Meletakkan inisialisasi `total_baris = 0` di luar loop luar (sebelum loop i dimulai). Akibatnya, `total_baris` terus terakumulasi dari baris-baris sebelumnya dan menghasilkan nilai total yang salah untuk baris berikutnya.
* **Cara Memperbaiki:** Memindahkan instruksi `total_baris = 0` ke dalam loop luar, tepat sebelum loop dalam (j) dimulai, agar nilainya selalu kembali ke 0 pada setiap awal baris baru.
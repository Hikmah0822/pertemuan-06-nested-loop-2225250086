# ==============================================================================
# Tugas 3: Tabel Perkalian dan Statistik
# File: tugas/tabel_perkalian_dan_statistik.py
# ==============================================================================

print("Tabel Perkalian dan Statistik")

# 1. Baca dan validasi n
n = int(input("n: "))
while n <= 0:
    print("Nilai n harus berupa bilangan bulat positif!")
    n = int(input("n: "))

# 2. Inisialisasi total keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# 3. Nested loop untuk membuat tabel perkalian n x n
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4d}", end="")
        
        # Akumulasi nilai per baris dan total keseluruhan
        total_baris += hasil
        total_semua += hasil
        
        # Pencacahan nilai genap
        if hasil % 2 == 0:
            count_genap += 1
            
    # Tampilkan jumlah per baris di sebelah kanan tabel
    print(f"  | Jumlah baris {i} = {total_baris}")

# 4. Output statistik akhir
print("-" * 45)
print(f"Total keseluruhan  = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
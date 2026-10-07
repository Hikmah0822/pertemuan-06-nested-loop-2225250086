# Loop luar menentukan baris.
# Loop dalam menghitung hasil i * j.
# total_baris menjadi akumulator untuk setiap baris.
# Output menampilkan jumlah setiap baris.

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        total_baris += i * j

    print(f"Jumlah baris {i} = {total_baris}")
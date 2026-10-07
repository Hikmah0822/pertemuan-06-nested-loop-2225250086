# ==============================================================================
# Latihan 4: Menghitung Pasangan
# Peran komponen:
# - Loop Luar : Mengiterasi nilai i dari 1 hingga n.
# - Loop Dalam: Mengiterasi nilai j dari 1 hingga n.
# - Kondisi   : `if i + j <= n` memeriksa apakah jumlah pasangan tidak melebihi n.
# - Counter   : 'count' bertambah 1 hanya jika pasangan (i, j) memenuhi kondisi.
# - Output    : Menampilkan total pasangan yang memenuhi kondisi.
# ==============================================================================

n = int(input("n: "))
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")
# Loop luar menentukan nomor baris.
# Loop dalam mencetak bintang sesuai nomor baris.
# Output berupa pola segitiga.

n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
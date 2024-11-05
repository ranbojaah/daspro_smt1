# while True:
#     angka = int(input("Masukkan angka yang lebih dari 5: "))
#     if angka > 5:
#         print("Angka yang Anda masukkan adalah:", angka)
#         break
#     else:
#         print("Angka yang Anda masukkan kurang dari 5. Silakan coba lagi!")

n = int(input("Masukkan jumlah baris: "))

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
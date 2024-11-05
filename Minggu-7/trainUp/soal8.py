# list1 = ["a", "b", "c", "d", "e",]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # print(list1+list2)

# Program untuk mencetak deret Fibonacci bertingkat
n = 10  # Jumlah baris yang ingin ditampilkan

a, b = 0, 1
for i in range(1, n + 1):
    print(" ".join(str(a) for _ in range(i)))
    a, b = b, a + b

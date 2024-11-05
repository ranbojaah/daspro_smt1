# Zahran Faiz Salman - 2404754 - RPL 1 A

print("1.Buatlah program untuk mengambil list ke 2-5")
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(buah[2:6])

print("\n2.Hapus item “apel“ yang kedua")
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah.pop(4)
print(buah)

print("\n3.Ganti item dengan nama `ceri` menjadi `cherry`")
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah[2] = "cherry"
print(buah)

print("\n4.Tambahkan item dengan nama `strawberry` ke dalam index ke-3") 
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah.insert(3, "strawberry")
print(buah)

print("\n5.Urutkan item pada list sesuai dengan abjadnya")
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah.sort()
print(buah)




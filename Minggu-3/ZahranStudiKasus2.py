# Zahran Faiz Salman - 2404754 - RPL 1 A

print("1. Buatlah program untuk mengambil tuple ke 2-5")
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
print(buah[2:6])

print("\n2. Manipulasi tuple buah agar item “durian” dapat dihapus")
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
a = list(buah)
a.pop(3)
buah = tuple(a)
print(buah)

print("\n3. Manipulasi tuple buah agar ada tambahan item `manggis` diantara item `jeruk` dan `ceri`")
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
a = list(buah)
a.insert(2, "manggis")
buah = tuple(a)
print(buah)
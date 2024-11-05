# Meminta pengguna untuk memasukkan angka
angka = float(input("Masukkan angka: "))

# Percabangan untuk menentukan jenis angka
if angka > 0:
    print("Angka tersebut adalah bilangan positif.")
elif angka < 0:
    print("Angka tersebut adalah bilangan negatif.")
else:
    print("Angka tersebut adalah nol.")

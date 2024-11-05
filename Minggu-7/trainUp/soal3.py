# Tampilkan apakah angka tersebut bilangan prima atau bukan.

angka = int(input("Masukkan angka: "))

for i in range(2, angka):
  if angka % i == 0:
    print(f"{angka} bukan bilangan prima")
    break
else:
  print(f"{angka} adalah bilangan prima")
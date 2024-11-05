n = int(input("Masukkan angka: "))

for i in range(n+1):
  if i % 2 == 0:
    continue
  print(i)
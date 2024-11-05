# Memasukkan harga barang

hargaBarang = int(input("Masukkan harga barang: "))

if hargaBarang > 500000:
  diskon = 20/100
elif hargaBarang >= 100000:
  diskon = 10/100
else:
  diskon = 0
  
total = (1 - diskon) * hargaBarang
print(f'Rp{float(total)}')
jenisKendaraan = input("Masukkan jenis kendaraan: ").lower()
hargaKendaraan = int(input("Masukkan harga kendaraan: "))

pajak = 0
if jenisKendaraan == "mobil":
  pajak = 10 / 100
elif jenisKendaraan == "motor":
  pajak = 5 / 100
else:
  print("Jenis kendaraan tidak dikenali")

if pajak > 0:
  print(f"Total pajak: {hargaKendaraan * pajak}")


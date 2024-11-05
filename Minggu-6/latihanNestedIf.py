# Zahran Faiz Salman - 2404754 - RPL 1A

nilai = int(input("Masukkan nilai: "))

if (nilai > 0): 
  if(nilai % 2 == 0):
    print(f"{nilai} adalah bilangan positif dan termasuk bilangan genap")
  else:
    print(f"{nilai} adalah bilangan positif dan termasuk bilangan ganjil")
elif (nilai < 0):
  if(nilai % 2 == 0):
    print(f"{nilai} adalah bilangan negatif dan termasuk bilangan genap")
  else:
    print(f"{nilai} adalah bilangan negatif dan termasuk bilangan ganjil")
else:
  print(f"{nilai} adalah bilangan nol")
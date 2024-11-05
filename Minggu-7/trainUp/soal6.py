nilai1 = int(input("Masukkan nilai 1: "))
nilai2 = int(input("Masukkan nilai 2: "))
nilai3 = int(input("Masukkan nilai 3: "))
nilai4 = int(input("Masukkan nilai 4: "))
nilai5 = int(input("Masukkan nilai 5: "))

avarage = (nilai1+nilai2+nilai3+nilai4+nilai5)/5
print()

if avarage >= 85:
  klasifikasi = "Sangat Baik"
elif avarage >= 70 and avarage < 85:
  klasifikasi = "Baik"
elif avarage >= 50 and avarage < 70:
  klasifikasi = "Cukup"
else :
  klasifikasi = "Kurang"
  
print(f"Rata-rata nilai: {avarage}")
print(f"Klasifikasi: {klasifikasi}")
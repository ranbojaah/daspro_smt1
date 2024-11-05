# Zahran Faiz Salman - 2404754 - RPL 1A

nilai = {
  "1" : 78,
  "2" : 90,
  "3" : 56,
  "4" : 98,
  "5" : 65,
  "6" : 38,
  "7" : 42, 
  "8" : 74,
  "9" : 89,
  "10" : 90
}

absen = input("Masukan no absen: ")
data = nilai.get(absen)
print(f"Nilai absen {absen} adalah {data}")
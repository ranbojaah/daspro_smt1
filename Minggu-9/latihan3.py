# Zahran Faiz Salman - 2404754 - 1A

def selisihWaktu(jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai):
  totalDetikMulai = jamMulai * 3600 + menitMulai * 60 + detikMulai
  totalDetikSelesai = jamSelesai * 3600 + menitSelesai * 60 + detikSelesai
  
  selisih = totalDetikSelesai - totalDetikMulai
  
  jam = selisih // 3600
  menit = (selisih % 3600) // 60
  detik = (selisih % 3600) % 60
  
  return jam, menit, detik

print("Input mulai:")
jamM = int(input("Jam: "))
menitM = int(input("Menit: "))
detikM = int(input("Detik: "))
print("\nInput selesai:")
jamS = int(input("Jam: "))
menitS = int(input("Menit: "))
detikS = int(input("Detik: "))

jam, menit, detik = selisihWaktu(jamM, menitM, detikM,jamS, menitS, detikS)
print("\nHitung selisih:")
print(f"{jam} jam - {menit} menit - {detik} detik ")
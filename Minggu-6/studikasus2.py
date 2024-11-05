# Zahran Faiz Salman - 2404754 - RPL 1A

nama = input("Masukkan nama: ")
jk = input("Masukkan jenis kelamin (pria/wanita): ").lower()
umur = int(input("Masukkan umur: "))
iq = int(input("Masukkan iq: "))
tb = int(input("Masukkan tinggi badan: "))

if (jk == "pria" ):
  if (18 <= umur <= 25) and (iq >= 130) and (tb >= 175):
    print(f"{nama} anda dapat menjadi seorang model catwalk")
  else:
    print(f"{nama} anda tidak dapat menjadi seorang model catwalk")
elif (jk == "wanita"):
  if (18 <= umur <= 25) and (iq >= 130) and (tb >= 170):
    print(f"{nama} anda dapat menjadi seorang model catwalk")
  else:
    print(f"{nama} anda tidak dapat menjadi seorang model catwalk")
else:
  print("Input tidak valid")


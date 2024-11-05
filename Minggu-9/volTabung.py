# Zahran Faiz Salman - 2404754 - 1A

def volumeTabung(r,t):
    hasil = 3.14 * r * r * t
    return hasil
  
x = float(input("Masukkan jari-jari: "))
y = float(input("Masukkan tinggi: "))

volume = volumeTabung(x,y)
print(f"Volume tabung adalah: {volume}")



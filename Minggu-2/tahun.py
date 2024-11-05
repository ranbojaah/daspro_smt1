# Zahran Faiz Salman - 2404754 - RPL 1A
from datetime import datetime

nama = input("Masukkan nama: ")
tahun = int(input("Tahun Kelahiran: "))
current_year = datetime.now().year
umur = current_year - tahun
print(f"Selamat datang {nama}, Umur kamu sekarang {umur}")
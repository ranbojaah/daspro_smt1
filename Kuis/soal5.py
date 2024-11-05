# Zahran Faiz Salman - 2404754 - RPL 1A

mobil = {
    "Merk" : "Honda",
    "Tipe" : "HRV",
    "Tahun" : "2018",
    "Warna" : "Hitam",
    "No. Polisi" : "D 1234 ABC",
    "Bensin" : "Pertalite",
    "Transmisi" : "Manual"
}

print("\nMobil lama Pak Oki adalah:")
print(f"Merk: {mobil["Merk"]}")
print(f"Tipe: {mobil["Tipe"]}")
print(f"Warna: {mobil["Warna"]}")
print(f"Tahun: {mobil["Tahun"]}")

print("\nMasukkan informasi detail mobil baru")
mobil["Merk"] = input("Merk: ")
mobil["Tipe"] = input("Tipe mobil: ")
mobil["Tahun"] = input("Tahun keluaran: ")
mobil["Warna"] = input("Warna: ")
mobil["No. Polisi"] = input("No. Polisi: ")
mobil["Bensin"] = input("Bensin: ")
mobil["Transmisi"] = input("Transmisi: ")

print("\nMobil baru Pak Oki adalah:")
print(f"Merk: {mobil["Merk"]}")
print(f"Tipe: {mobil["Tipe"]}")
print(f"Warna: {mobil["Warna"]}")
print(f"Tahun: {mobil["Tahun"]}")

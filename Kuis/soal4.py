# Zahran Faiz Salman - 2404754 - RPL 1A

barangJuli = ["Kerudung", "Kemeja", "Rok", "Celana Panjang", "Baju Renang", "Topi", "Tas", "Sepatu", "Kacamata"]

print("Barang jualan bulan juli:")
print("\n".join(barangJuli))
print(f"Jumlah barang yang dijual bulan juli adalah {len(barangJuli)}")

barangJuli.remove("Baju Renang")
barangJuli.append("Piyama")
barangJuli.append("Ikat Rambut")
barangJuli.append("Sendal")

print("\nBarang jualan bulan agustus:")
print("\n".join(barangJuli))
print(f"Jumlah barang yang dijual bulan agustus adalah {len(barangJuli)}")

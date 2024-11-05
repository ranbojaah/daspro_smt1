# Zahran Faiz Salman - 2404754 - RPL 1A

stundent_info = {
  "Alice" : {"age" : 20, "major" : "Computer Science"},
  "Bob" : {"age" : 21, "major" : "Mathematics"},
  "Charlie" : {"age" : 19, "major" : "Physics"},
}

name = input("Masukkan nama siswa: ")
info = stundent_info.get(name)

print(f"Umur {name} adalah {info["age"]} dan Prodi nya adalah {info["major"]}")
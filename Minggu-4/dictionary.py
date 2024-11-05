# Membuat dictionary
my_dict = {
    "nama": "Zahran",
    "usia": 20,
    "jurusan": "Rekayasa Perangkat Lunak"
}

# Mengakses nilai berdasarkan key
nama = my_dict["nama"]
print("Nama:", nama)

# Menambahkan elemen ke dalam dictionary
my_dict["universitas"] = "UPI"

# Mengubah nilai
my_dict["usia"] = 21

# Menghapus elemen berdasarkan key
del my_dict["jurusan"]

# Iterasi melalui key dan value
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

buah = {
    "nama" : "kucing", 
    "jenis" : "persian", 
    "hidup" : True, 
    "menghapus" : False
    }

print(buah.get("nama"))
print(buah.values())
# buah["jenis"] = "amba"
# buah["mengapa"] = "begitu"
buah.update(
    {
        "jenis": "negroid",
        "menghapus": True
    }
    )

x = buah.items()
print(x)
for key, value in buah.items():
    print(f"{key}: {value}")
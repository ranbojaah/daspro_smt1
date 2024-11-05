# Membuat set dengan beberapa elemen
my_set = {1, 2, 3, 4, 5, 5}  # Duplikasi elemen akan dihapus otomatis

# Menambahkan elemen ke dalam set
my_set.add(6)

# Menghapus elemen dari set
my_set.remove(1)

# Mengecek apakah elemen ada di dalam set
if 3 in my_set:
    print("3 ada di dalam set")

# Menggunakan operasi himpunan
another_set = {4, 5, 6, 7}

# Union (gabungan)
union_set = my_set.union(another_set)

# Intersection (irisan)
intersection_set = my_set.intersection(another_set)

# selisih
differnce_set = my_set.symmetric_difference(another_set)

print("Set awal:", my_set)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", differnce_set)

s = {"apple", "orange", "green", "blue"}
c = ("banana", "black", "orange", "green", "red")
b = set(c)
# s.update(c)

print(b)
#Zahran Faiz Salman - 2404754 - RPL 1A

students = {
    "Alice" : "Computer Science",
    "Bob" : "Mathematics",
    "Charlie" : "Physics",
    "David" : "Computer Science",
    "Eva" : "Mathematics"
  }

val = list(students.values())
count_cs = val.count("Computer Science")
count_math = val.count("Mathematics")
count_pysc = val.count("Physics")

result = {
    "Prodi computer science sebanyak" : count_cs,
    "Prodi mathematics sebanyak" : count_math,
    "Prodi physics sebanyak" : count_pysc
  }

for key, value in result.items():
    print(f"{key}: {value}")
operator = input('Masukkan operator "penambahan", "pengurangan", "perkalian" atau "pembagian": ').lower()

number1 = int(input('Masukkan angka pertama: '))
number2 = int(input('Masukkan angka kedua: '))

if operator == "penambahan":
  hasil = number1 + number2
elif operator == "pengurangan":
  hasil = number1 - number2
elif operator == "perkalian":
  hasil = number1 * number2
elif operator == "pembagian":
  hasil = number1/number2
else:
  print("Operator tidak dikenali")
  
print(f'Hasil {operator}: {hasil}')
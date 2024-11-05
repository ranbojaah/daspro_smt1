def segitiga_inverse(n):
  for i in range(1, n):
    for j in range(1, i+1):
      print("*", end="")
    print()

segitiga_inverse(5)
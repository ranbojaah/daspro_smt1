# Zahran Faiz Salman - 2404754 - 1A

def total_ratarata(*args):
    total = sum(args)
    rata_rata = total / len(args)
    return total, rata_rata
  
nilai = []
while True:
    input_nilai = input("Masukkan nilai (atau 'selesai' untuk berhenti): ")
    if input_nilai.lower() == 'selesai':
        break
    if input_nilai.isdigit():
        nilai.append(int(input_nilai))
    else:
        print("Input tidak valid. Silakan masukkan nilai yang benar.")

total, rata_rata = total_ratarata(*nilai)
print(f"Jumlah: {total}")
print(f"Rata-rata: {rata_rata}")

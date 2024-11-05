class Pelanggan:
    def __init__(self):
        self.member = False

    def set_member(self, member):
        self.member = member

    def get_member(self):
        return self.member

class Makanan:
    def __init__(self):
        self.menu = {}
        self.makanan = ""
        self.harga = 0

    def load_menu(self, filename):
        """Load menu from a text file."""
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(',')
                menu_id = int(data[0])
                self.menu[menu_id] = {
                    'nama': data[1],
                    'harga_non_member': int(data[2]),
                    'harga_member': int(data[3])
                }

    def set_pesan(self, pesan, pelanggan):
        """Set pesan berdasarkan input pengguna."""
        if pesan in self.menu:
            self.makanan = self.menu[pesan]['nama']
            if pelanggan.get_member():
                self.harga = self.menu[pesan]['harga_member']
            else:
                self.harga = self.menu[pesan]['harga_non_member']

    def get_harga(self):
        return self.harga

    def get_makanan(self):
        return self.makanan

    def tambah_menu(self, filename):
        """Tambah menu baru ke dalam file dan menu dict."""
        try:
            new_id = max(self.menu.keys()) + 1  # ID baru otomatis berdasarkan ID terakhir
        except ValueError:
            new_id = 1  # Jika menu.txt kosong, mulai dari 1
        
        nama = input("Masukkan nama makanan: ")
        harga_non_member = int(input("Masukkan harga non-member: "))
        harga_member = int(input("Masukkan harga member: "))

        # Tambahkan menu ke dictionary
        self.menu[new_id] = {
            'nama': nama,
            'harga_non_member': harga_non_member,
            'harga_member': harga_member
        }

        # Tambahkan menu ke file txt
        with open(filename, "a") as file:
            file.write(f"{new_id},{nama},{harga_non_member},{harga_member}\n")

        print(f"Menu {nama} berhasil ditambahkan!")

def main():
    pelanggan = Pelanggan()
    makan = Makanan()
    total = 0

    # Load menu from the file
    filename = "menu.txt"
    makan.load_menu(filename)

    while True:
        print("*******************************************")
        print("----------------Menu Makanan---------------")
        print("*******************************************")
        for key, value in makan.menu.items():
            print(f"{key}. {value['nama']} Rp.{value['harga_non_member']} (Member: Rp.{value['harga_member']})")
        print("*******************************************")
        print("1. Pesan Makanan")
        print("2. Tambah Menu Baru")
        print("3. Keluar")

        pilihan = input("Pilih tindakan (1-3): ")

        if pilihan == "1":
            member_status = input("Member? true/false: ").lower()
            pelanggan.set_member(member_status == "true")

            while True:
                order = int(input("Pilih Menu Makanan (1-3): "))
                makan.set_pesan(order, pelanggan)
                jumlah = int(input("Jumlah Beli: "))

                subtotal = makan.get_harga() * jumlah
                total += subtotal

                print("-------------------List-------------------")
                print(f"Menu Dipilih: {makan.get_makanan()}")
                print(f"Total: Rp.{subtotal}")
                print("=================================================")

                pesan_lagi = input("Pesan Lagi? (ya/tidak): ").lower()
                print("=================================================")

                if pesan_lagi == "tidak":
                    break

            print("-------------------Struk-------------------")
            print(f"Total Harga: Rp.{total}")
            uang = float(input("Masukkan Uang: Rp."))
            print(f"Kembalian: Rp.{uang - total}")
            print("-----------------Terima Kasih----------------")

        elif pilihan == "2":
            makan.tambah_menu(filename)

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()

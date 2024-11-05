# Zahran Faiz Salman - 2404754 - 1A

inputUsername = input("Username: ")
def login(password):
    token = 3
    while token > 0:
        inputPassword = input("Password: ")
        if inputPassword == password:
            print("Selamat datang di aplikasi")
            break
        else:
            token -= 1
            print(f"Login Salah! Kesempatan anda {token}x lagi")
            if token == 0:
                print("Anda tidak diperkenankan mengakses aplikasi ini.")

# Parameters for username and password
login_username = "Daspro2024"
login_password = "Latihan"

# Calling the login function
login(login_password)

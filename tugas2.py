def pw():
    password="Latihan" #password saved
    return password

def login():
    attempt = 3 # attempt sets to 3
    while True:
        attempt -= 1 # -1 attempt every login failed
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if password == pw():
            print("Selamat!, Kamu berhasil login")
            break
        else:
            if attempt == 0: # condition when attempt is 0
                print("Maaf, kamu telah mencoba 3 kali. Silakan coba lagi nanti!")
                break
            elif 0 < attempt < 3:
                print(f"Maaf, password salah. Anda memiliki {attempt} kesempatan lagi! ")
            else:
                break
login()


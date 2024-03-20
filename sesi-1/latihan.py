import random

random = random.randint(1, 10)
welcome = "Selamat datang di game tebak angka"

print("=======================================")
print(welcome)
print("=======================================")
input_user = input("Masukkan nama anda: ")
print("=======================================")
print(f"Selamat bermain {input_user}")
print("=======================================")
tebakan_angka = int(input("Tebak angka dari 1-10: ")) # sudah di convery ke integer, karena bawaan input tipe data string
print("=======================================")
confirm_message = input(f"Apakah angka {tebakan_angka} sudah benar? (y/n): ")
print("=======================================")
if confirm_message == "y":
    if tebakan_angka == random:
        print("Selamat, tebakan anda benar")
    else:
        print(f"Maaf, tebakan anda salah. Angka yang benar adalah {random}")
elif confirm_message == "n":
    print("Anda membatalkan permainan")
    exit()
else :
    print("Inputan tidak valid, program berhenti")
    exit()


import random

random = random.randint(1, 10)
welcome = "Selamat datang di game tebak angka"

print("=======================================")
print(welcome)
print("=======================================")
gambar = "|_|"
goa = [gambar] * 10 # ! Goa Asli

temporary_goa = goa.copy() # ! Goa yang sudah diubah
temporary_goa[random - 1] = "|X|"

join_goa = " ".join(temporary_goa)

input_user = input("Masukkan nama anda: ")
print("=======================================")
print(f"Selamat bermain {input_user}")
print("=======================================")
tebakan_angka = int(input(f"{goa} \n Tebak angka Goa dari 1-10: ")) # sudah di convery ke integer, karena bawaan input tipe data string
print("=======================================")
confirm_message = input(f"Apakah angka {tebakan_angka} sudah benar? (y/n): ")
print("=======================================")
if confirm_message == "y":
    if tebakan_angka == random:
        print(f"Selamat, tebakan anda benar. \n {join_goa}")
    else:
        print(f"Maaf, tebakan anda salah. \n {join_goa}")
elif confirm_message == "n":
    print("Anda membatalkan permainan")
    exit()
else :
    print("Inputan tidak valid, program berhenti")
    exit()
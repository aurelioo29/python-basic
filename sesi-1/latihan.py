import random

random = random.randint(1, 10)
welcome = "Selamat datang di game tebak angka"

print(welcome)
input_user = input("Masukkan nama anda: ")
print(f"Selamat bermain {input_user} \n")
tebakan_angka = int(input("Tebak angka dari 1-10: ")) # sudah di convery ke integer, karena bawaan input tipe data string
print("\n")
if tebakan_angka == random:
    print("Selamat, tebakan anda benar")
else:
    print(f"Maaf, tebakan anda salah. Angka yang benar adalah {random}")


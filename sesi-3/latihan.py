import random
import sys
sys.path.insert(0, 'D:/Coding/website/python_basic/package')  # Using forward slashes 
import library

goa = ["|_|"] * 10  # Goa Asli

library.message_come("Permainan Tebak Angka Goa")

input_user = input("Masukkan nama anda: ")
while input_user == "":
    input_user = input("(Nama tidak boleh kosong) Masukkan nama anda: ")

print(f"Selamat bermain {input_user}")

while True:
    random_number = random.randint(1, 10)  # Menghasilkan nomor acak baru setiap kali permainan dimulai
    temporary_goa = goa.copy()  # Goa yang sudah diubah
    temporary_goa[random_number - 1] = "|X|"
    join_goa = " ".join(temporary_goa)

    tebakan_angka = int(input(f"{goa} \n Tebak angka Goa dari 1-10: "))  # Sudah di convert ke integer, karena bawaan input tipe data string
    while tebakan_angka < 1 or tebakan_angka > 10:
        input_user = input("(Angka tidak terdeteksi) Masukkan angka Goa dari 1-10: ")
        tebakan_angka = int(input_user)
    confirm_message = input(f"Apakah angka {tebakan_angka} sudah benar? (y/n): ")
    if confirm_message == "y":
        if tebakan_angka == random_number:
            print(f"Selamat, tebakan anda benar. \n {join_goa}")
        else:
            print(f"Maaf, tebakan anda salah. \n {join_goa}")
    elif confirm_message == "n":
        print("Anda membatalkan permainan")
        exit()
    else:
        print("Inputan tidak valid, program berhenti")
        exit()
    # * Validate user want to play again
    confirm_message = input("Apakah anda ingin bermain lagi? (y/n): ")
    if confirm_message == "n": # Jika inputan "n"
        break
    else: # Jika inputan selain "n / y"
        exit()

print("Terima kasih sudah bermain")
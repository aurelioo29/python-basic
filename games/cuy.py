import random

def start():
  while True:
      goa = ["|_|"] * 10  # Goa Asli
      random_number = random.randint(1, 10)  # Menghasilkan nomor acak baru setiap kali permainan dimulai
      temporary_goa = goa.copy()  # Goa yang sudah diubah
      temporary_goa[random_number - 1] = "|X|"
      join_goa = " ".join(temporary_goa)

      tebakan_angka = int(input(f"\n{goa}\n\nTebak angka Goa dari [1-10]: "))  # Sudah di convert ke integer, karena bawaan input tipe data string
      
      while tebakan_angka < 1 or tebakan_angka > 10:
          input_user = input("(Angka tidak terdeteksi) Masukkan angka Goa dari [1-10]: ")
          tebakan_angka = int(input_user)

      if tebakan_angka == random_number:
          print(f"\nSelamat, tebakan anda benar. \n\n{join_goa}")
      else:
          print(f"\nMaaf, tebakan anda salah. \n\n{join_goa}")

      # * Validate user want to play again
      confirm_message = input("\nApakah anda ingin bermain lagi? (y/n): ")
      if confirm_message == "n": # Jika inputan "n"
          break
      
  print("Terima kasih sudah bermain")
  
if __name__ == "__main__":
  start()
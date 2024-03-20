# deklarasi variabel
welcome_message = "Selamat datang di Program Python Dasar"

print(welcome_message)
print(f"{welcome_message} versi format string\n")

# condition
angka = 10

if angka > 5:
    print("Angka lebih dari 5 \n")
else:
    print("Angka kurang dari 5 \n")
    
# menampung inputan user
nama_user = input("Masukkan nama anda: ")
print(f"Nama anda adalah {nama_user}")

# print multibaris
print(""" 
      Ini adalah
      contoh print
      """)

# cek type data

data1 = "10"
data2 = 10

print(type(data1))
print(type(data2))
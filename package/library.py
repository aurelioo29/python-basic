import socket
from time import sleep

pc_name = socket.gethostname()

def message_come():
  garis = "-" * (len(pc_name) + 10)
  print(garis)
  print(f"---- {pc_name} ----")
  print(garis)

def exit_program():
  print("Program akan keluar dalam 3 detik")
  sleep(3 )

if __name__ == 'main':
  message_come()

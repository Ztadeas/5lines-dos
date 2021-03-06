import subprocess

while True:
  sub1 = subprocess.run(["ping", "81.0.198.205"], capture_output=True, shell=True)

  p = sub1.stdout.decode()

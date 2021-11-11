# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:48:32 2020

@author: edala
"""
import des_full, des3_aes, rsa, playfair, hill, row_transposition, caesar, vigenere, feistel

print("\nWelcome to CodeBreak. The following algorithm decryptions are possible.\n")
print("1. Playfair cipher")
print("2. Hill cipher")
print("3. Row transposition cipher")
print("4. Caesar cipher")
print("5. Data Encryption Standard")
print("6. Triple Data Encryption Standard")
print("7. Advanced Encryption Standard")
print("8. Rivest Shamir Adleman")
print("9. Vigenere cipher")
print("10. Feistel cipher")

choice = 0
while True:
    try:
        choice = int(input("Enter the index number of the decryption algorithm required: "))
    except:
        print("Invalid input. Try again.")
    else:
        break

if (choice == 1):
    key = input("Enter the key: ")    # Example key: "Sample key"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "RI DL DL MA XS BN NS SB NP KE NB QL DE AM DY"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", playfair.decryptor(key, message))
    
if (choice == 2):
    hill.decryptor() # Example key: "HILL", Example ciphertext: "CVUCUCQQTNHLOGTVDHYKMEOOXB"
    
if (choice == 3):
    key = int(input("Enter the key: "))    # Example key: "8"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "Cenoonommstmme oo snnio. s s c"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", row_transposition.decryptor(key, message))
    
if (choice == 4):
    key = int(input("Enter the key: "))    # Example key: "3"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "wrehruqrwwreh"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", caesar.decryptor(key, message))

if (choice == 5):
    ciphertext = input("Enter your text: ") # Example text: "C0B7A8D05F3A829C"
    key = input("Enter the round key: ") # Example key: "AABB09182736CCDD"
    print("\n BEGINNING DECRYPTION PROCESS \n")
    print("\nThe plaintext is:", des_full.decryption(ciphertext, key))
    
if (choice == 6 or choice == 7):
    ciphertext = input("Enter any text: ") # Example input: "0123456789abcdef"
    key = input("Enter any 16 or 24 byte key: ") # Example key: "sixteen byte key"
    print("\nBEGINNING TRANSFORMATION PROCESS")
    if (choice == 6):
        des3_aes.decryption_DES3(ciphertext, key)
    else:
        des3_aes.decryption_AES(ciphertext, key)
        
if (choice == 8):
    rsa.decryptor()

if (choice == 9):
    key = input("Enter the key: ")   # Example key: "sample"
    message = input("Enter the ciphertext message: ")   # Example ciphertext: "lhuhtwlhqezawraugmyeztci"
    print("\nBEGINNING DECRYPTION PROCESS\n")
    print("The plaintext is", vigenere.decryptor(key, message))

if (choice == 10):
    message = input("Enter any text message: ")
    print("\nBEGINNING ENCRYPTION/DECRYPTION PROCESS\n")
    feistel.action(message)
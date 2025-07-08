### crypto-tool/main.py
from src.caesar import caesar_encrypt, caesar_decrypt
from src.vigenere import vigenere_encrypt, vigenere_decrypt
from src.rsa import generate_keypair, encrypt, decrypt

if __name__ == "__main__":
    print("Cryptography Tool")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. RSA Encryption")
    choice = input("Choose cipher [1-3]: ")

    if choice == '1':
        msg = input("Enter message: ")
        key = int(input("Enter key (number): "))
        encrypted = caesar_encrypt(msg, key)
        decrypted = caesar_decrypt(encrypted, key)
        print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")

    elif choice == '2':
        msg = input("Enter message: ")
        key = input("Enter keyword: ")
        encrypted = vigenere_encrypt(msg, key)
        decrypted = vigenere_decrypt(encrypted, key)
        print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")

    elif choice == '3':
        msg = input("Enter message: ")
        public, private = generate_keypair()
        print(f"Public key: {public}\nPrivate key: {private}")
        encrypted = encrypt(public, msg)
        decrypted = decrypt(private, encrypted)
        print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")


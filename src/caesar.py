### crypto-tool/src/caesar.py
def caesar_encrypt(text, key):
    text = text.upper()
    return ''.join(
        chr((ord(c) - 65 + key) % 26 + 65) if c.isalpha() else c for c in text
    )

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)
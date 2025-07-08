def vigenere_encrypt(text, key):
    text, key = text.upper(), key.upper()
    result = ''
    for i, c in enumerate(text):
        if c.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(c) - 65 + shift) % 26 + 65)
        else:
            result += c
    return result

def vigenere_decrypt(ciphertext, key):
    text, key = ciphertext.upper(), key.upper()
    result = ''
    for i, c in enumerate(text):
        if c.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(c) - 65 - shift + 26) % 26 + 65)
        else:
            result += c
    return result
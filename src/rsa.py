# ========================
# File: src/rsa.py
# ========================
from utils.mod_inverse import mod_inverse
from utils.prime_utils import is_prime, generate_prime

import random

def generate_keypair():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while mod_inverse(e, phi) is None:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)
# ========================
# File: utils/mod_inverse.py
# ========================
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        return None  # Modular inverse doesn't exist
    else:
        return x % phi

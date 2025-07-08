# ========================
# File: web/app.py
# ========================
import sys
import os
import base64
import streamlit as st

# Setup paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))

from src.caesar import caesar_encrypt, caesar_decrypt
from src.vigenere import vigenere_encrypt, vigenere_decrypt
from src.rsa import generate_keypair, encrypt as rsa_encrypt, decrypt as rsa_decrypt

# Set background
def set_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_bg_from_local("web/background.png")

# CSS for UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 900px;
        margin: auto;
        padding: 2rem;
        background-color: rgba(255, 255, 255, 0.88);
        border-radius: 16px;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.12);
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        font-size: 1rem;
        color: #343a40;
        padding: 0.6rem 1.5rem;
        border-radius: 10px 10px 0 0;
    }

    button[kind="primary"] {
        background-color: #4F8BF9;
        color: white;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header UI
st.markdown("<h1 style='text-align: center;'>🔐 Cryptography Tool</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Encrypt & Decrypt using Caesar, Vigenère, and RSA Ciphers</h4>", unsafe_allow_html=True)
st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["🔡 Caesar Cipher", "🗝️ Vigenère Cipher", "🛡️ RSA Encryption"])

with tab1:
    st.header("🔡 Caesar Cipher")
    msg = st.text_input("Enter message:", key="caesar_msg")
    key = st.number_input("Enter key (number):", step=1, value=3, key="caesar_key")
    if st.button("Encrypt Caesar"):
        encrypted = caesar_encrypt(msg, key)
        st.success(f"Encrypted: {encrypted}")
    if st.button("Decrypt Caesar"):
        decrypted = caesar_decrypt(msg, key)
        st.success(f"Decrypted: {decrypted}")

with tab2:
    st.header("🗝️ Vigenère Cipher")
    msg = st.text_input("Enter message:", key="vigenere_msg")
    keyword = st.text_input("Enter keyword:", key="vigenere_key")
    if st.button("Encrypt Vigenère"):
        encrypted = vigenere_encrypt(msg, keyword)
        st.success(f"Encrypted: {encrypted}")
    if st.button("Decrypt Vigenère"):
        decrypted = vigenere_decrypt(msg, keyword)
        st.success(f"Decrypted: {decrypted}")

with tab3:
    st.header("🛡️ RSA Encryption")
    msg = st.text_input("Enter message:", key="rsa_msg")
    if st.button("Generate Keys + Encrypt with RSA"):
        public_key, private_key = generate_keypair()
        encrypted = rsa_encrypt(public_key, msg)
        decrypted = rsa_decrypt(private_key, encrypted)
        st.code(f"Public Key: {public_key}\nPrivate Key: {private_key}\n\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

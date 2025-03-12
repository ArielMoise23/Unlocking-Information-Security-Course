from Crypto.Cipher import ARC4

def rc4(plaintext, key):
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext) 
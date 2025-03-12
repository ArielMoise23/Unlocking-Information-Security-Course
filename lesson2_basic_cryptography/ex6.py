from Crypto.Cipher import AES
from Crypto import Random

## seems for this exc no need to pad
# from Crypto.Util.Padding import pad, unpad
#     padded_plaintext = pad(plaintext, AES.block_size)
#     decrypted_padded = decipher.decrypt(ciphertext)
#     decrypted_text = unpad(decrypted_padded, AES.block_size)



def aes_encrypt(plaintext, k):
    iv = Random.get_random_bytes(16)
    cipher = AES.new(k, AES.MODE_CBC, iv)

    ciphertext = cipher.encrypt(plaintext)

    return iv + ciphertext
    # pass # return iv + ciphertext (in bytes)

def aes_decrypt(ciphertext, k):
    received_iv = ciphertext[:16]
    received_ciphertext = ciphertext[16:]

    decipher = AES.new(k, AES.MODE_CBC, received_iv)
    decrypted_text = decipher.decrypt(received_ciphertext)

    return decrypted_text.decode('latin1')
    # pass # return plaintext (in 'latin1')
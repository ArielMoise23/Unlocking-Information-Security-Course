
def vigenere_encrypt(plaintext, codeword):
    ciphertext = ""  
    codeword_repeated = (codeword * (len(plaintext) // len(codeword) + 1))[:len(plaintext)]

    for p, c in zip(plaintext, codeword_repeated):
        shift = ord(c) - ord('A')  # Calculate shift value
        encrypted_char = chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
        ciphertext += encrypted_char  

    return ciphertext

def hash(s):
    result = 0
    for c in s:
        result = (result + ord(c) * 3 + 17) % 791
    return result

print(hash("   >"))
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    for i in range(1, 27):
        print(decrypt(ciphertext, i))
        print(i)
    pass #print all (plaintext, k) possibilities and copy the right one to the Edx platform
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
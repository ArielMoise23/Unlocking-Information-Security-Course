from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
# from Root.prev_func import aes_decrypt, is_english
from ex6 import aes_decrypt, aes_encrypt
from ex7 import is_english

"""
Brute force a message encrypted with AES-CBC, given that it was encrypted with a 
key that represents a phone number of someone from Tel-Aviv, padded with zeroes 
(in other words, 9 digits, beginning with 036, and with trailing '0' to a length of 16 bytes,
 like this: 036######0000000).

You should test your brute-force cracker code using the outputs from your 
encrypt function of Hackxercise 6.


"""


def brute_force_aes(ciphertext):
    possible_keys = generate_keys()

    for k in possible_keys:
        option = aes_decrypt(ciphertext, k)
        if is_english(option):
            return option, k
    pass # return plaintext (in 'latin1', from aes_decrypt()), k

def generate_keys():
    keys = []
    
    for num in range(100000):
        len_of_zero = 9 - len("036" + str(num))
        phone_num =  "036" + "0" * (len_of_zero) + str(num) + "0" * 16
        key = phone_num.encode()[:16]
        keys.append(key)

    for num in range(1000000):
        phone_num = "036" + str(num)
        phone_num =  phone_num + "0" * 16
        
        key = phone_num.encode()[:16]
        keys.append(key)

    return keys


brute_force_aes(aes_encrypt("etaetaetaetaetaetaetaetaetaetaetaetaetaetaetaeta".encode(),b'0360001110000000'))

## import the functions im using from other exercises
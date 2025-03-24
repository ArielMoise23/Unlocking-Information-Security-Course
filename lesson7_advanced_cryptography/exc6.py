from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'

def weak_hmac(m, k, ipad, opad):

    if isinstance(m, str):
        m = m.encode('utf-8')
    

    key_xor_ipad = bytes(x ^ y for x, y in zip(k, ipad))
    first_hash_input = key_xor_ipad + m
    first_hash = sha1(first_hash_input).digest()
    key_xor_opad = bytes(x ^ y for x, y in zip(k, opad))
    second_hash_input = key_xor_opad + first_hash
    final_hash = sha1(second_hash_input).digest()
    
    return final_hash
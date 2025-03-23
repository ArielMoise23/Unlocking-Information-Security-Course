n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def encrypt(m, public_key):
    n, e = public_key
    return pow(m, e, n)  # m^e % n

def decrypt(c, private_key):
    n, d = private_key
    return pow(c, d, n)  # c^d % n

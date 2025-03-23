n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def sign(m, private_key):
    n, d = private_key
    return pow(m, e, n)

def verify(m, s, public_key):
    n, e = public_key
    return pow(s, d, n) == m

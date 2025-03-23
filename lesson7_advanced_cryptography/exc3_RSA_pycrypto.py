from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    pub_key = RSA.importKey(public_key)
    n = pub_key.n
    e = pub_key.e
    c = pow(m, e, n)
    return c

def decrypt(c, private_key):
    priv_key = RSA.importKey(private_key)
    n = priv_key.n
    d = priv_key.d
    m = pow(c, d, n)
    return m

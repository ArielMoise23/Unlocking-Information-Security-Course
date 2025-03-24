from Crypto.PublicKey import RSA

key = RSA.generate(2048)


private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def sign(m, private_key):
    key = RSA.importKey(private_key)
    n = key.n
    d = key.d
    s = pow(m, d, n)
    return s

def verify(m, s, public_key):
    key = RSA.importKey(public_key)
    n = key.n
    e = key.e
    m_prime = pow(s, e, n)
    return m == m_prime

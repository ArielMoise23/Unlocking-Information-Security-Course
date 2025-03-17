import hashlib

text = "Hello, world!".encode()

m = hashlib.md5(text)
sha1 = hashlib.sha1(text)
sha2 = hashlib.sha256(text)
# sha3 = hashlib.sha3_224(text)

print(m.hexdigest())
print(sha1.hexdigest())
print(sha2.hexdigest())

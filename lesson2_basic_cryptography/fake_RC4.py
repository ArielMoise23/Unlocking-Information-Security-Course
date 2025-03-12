def get_prg(plaintext_size, k):
    # convert key and plaintext to byte arrays if there strings
    if isinstance(k, str):
        k = [ord(c) for c in k]

    # a copy to modify
    key_copy = k.copy()
    key_length = len(key_copy)

    # initializing
    i = 0
    j = 0

    keystream = []

    # generating keystream in the lenght of plaintext
    for _ in range(plaintext_size):
        i = (i + 1) % key_length
        j = (j + key_copy[i]) % key_length

        key_copy[i], key_copy[j] = key_copy[j], key_copy[i]

        keystream_index = (key_copy[i] + key_copy[j]) % key_length

        keystream_char = key_copy[keystream_index]

        keystream.append(chr(keystream_char))

    return "".join(keystream)

def fake_rc4(plaintext, keystream):

    if isinstance(plaintext, str):
        plaintext = [ord(c) for c in plaintext]

    if isinstance(keystream, str):
        keystream = [ord(c) for c in keystream]

    if len(keystream) < len(plaintext):
        raise ValueError("keystream too short")
    
    cyphertext = []
    keystream_lst = list(keystream)
    for i in range(len(plaintext)):
        cypher_byte = plaintext[i] ^ int(keystream_lst[i])
        cyphertext.append(cypher_byte)
    

    return bytes(cyphertext).decode(errors="ignore") 


# TEST
if __name__ == "__main__":
    # Get the keystream
    keystream = get_prg(50, "abcdefghijabcdefghijabcdefghij12")
    encrypted1 = fake_rc4("12345678901234567890123456789012345678901234567890", keystream)
    
    ## second test - 
    keystream2 = get_prg(6, "12345678901234567890123456789012")
    #output "201133"

    # Encrypt the plaintext
    encrypted = fake_rc4("Hello!", keystream2)
    print("Encrypted (hex):", encrypted.hex())
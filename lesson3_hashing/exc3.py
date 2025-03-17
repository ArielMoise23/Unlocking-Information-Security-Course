from exc2 import simple_hash

"""
Brute-force the hash function you've just written!

Implement a function crack that given a string s,
loops until it finds a different string that collides with it, and returns the different string.
"""


def crack(s):
    orginal_hash_value = simple_hash(s)
    
    
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Alphabet string
    for first in letters:
        for second in letters:
            for third in letters:
                word = first + second + third
                try_hash = simple_hash(word)
                if try_hash == orginal_hash_value and word != s:
                    return word
    return "FAIL"
    # return # return s2 such that s != s2 and simple_hash(s) == simple_hash(s2)


print(crack("bar"))
"""
The function weak_md5 is a "weaker" version of MD5, using only the first 5 bytes of the MD5 hash. This means its hashing size is  𝑛=40  
and it can be brute forced rather easily.

Implement a function find_collisions that loops over all the possible strings until it finds an arbitrary collision - that is, 
two different strings whose hash is the same - and returns them (as a tuple).

"""

import hashlib


def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    dict_of_hashes = {}

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Alphabet string
    found = False

    for first in letters:
        found = check_hashing(first, dict_of_hashes)
        if found:
            return found

    while not found:
        dict_of_hashes_copy = dict_of_hashes.copy()
        for value in dict_of_hashes_copy.values():
            for letter in letters:
                found = check_hashing(value + letter, dict_of_hashes)
                if found:
                    return found

def check_hashing(word, dict_of_hashes):
    hash_value = weak_md5(word.encode())

    if hash_value in dict_of_hashes:
        if dict_of_hashes[hash_value] != word:
            return (dict_of_hashes[hash_value], word)

    dict_of_hashes[hash_value] = word
    return False

                        
print(find_collisions())
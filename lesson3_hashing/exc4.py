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
    # return # return (s1, s2) such that s1 != s2 and weak_md5(s1) == weak_md5(s2)

    dict_of_hashes = {}


    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Alphabet string
    for first in letters:
        is_found = check_hashing(first, dict_of_hashes)
        if is_found:
            return is_found
        for second in letters:
            is_found = check_hashing(first + second, dict_of_hashes)
            if is_found:
                return is_found
            for third in letters:
                is_found = check_hashing(first + second + third, dict_of_hashes)
                if is_found:
                    return is_found
                for forth in letters:
                    is_found = check_hashing(first + second + third + forth, dict_of_hashes)
                    if is_found:
                        return is_found
                    for fifth in letters:
                        word = first + second + third + forth + fifth
                        is_found = check_hashing(word, dict_of_hashes)
                        if is_found:
                            return is_found

def check_hashing(word, dict_of_hashes):
    hash_value = weak_md5(word.encode())

    if hash_value in dict_of_hashes:
        return (dict_of_hashes[hash_value], word)

    dict_of_hashes[hash_value] = word

                        
find_collisions()
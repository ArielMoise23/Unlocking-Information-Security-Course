alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    list_alph = list_to_str_with_separator(alphabet)
   
    original_txt = str_to_list_of_chars(plaintext)
    new_text = []

    for char in original_txt:
        if char == ' ':
            new_text.append(char)
        else:
           positions = [i for i, alphaChar in enumerate(list_alph) if alphaChar == char][0]
           new_text.append(list_alph[positions - k] )


    return list_to_str_with_separator(new_text)
#    pass # do stuff and return ciphertext

def list_to_str_with_separator(lst, separator=''):
    return separator.join(map(str, lst))

def str_to_list_of_chars(s):
    return [char for char in s]


print(encrypt('my name is ariel', 2))
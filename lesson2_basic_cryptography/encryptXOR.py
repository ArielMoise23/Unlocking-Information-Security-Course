def encrypt(plaintext, k):
    binary_plaintext = string_to_binary(plaintext)
    binary_k = string_to_binary(k)

    result = []
    p_index = 0  # Index for the clean plaintext
    
    for char in binary_plaintext:
        if char == " ":
            # If it's a space, keep it as a space
            result.append(" ")
        else:
            # Get corresponding bits and perform XOR
            if binary_k[p_index] == ' ':
                result.append(" ")
            else:
                p_bit = int(binary_plaintext[p_index])
                k_bit = int(binary_k[p_index])
                xor_result = p_bit ^ k_bit  # Python's XOR operator
                result.append(str(xor_result))
        p_index += 1
    return binary_to_string(str("".join(result)))

def string_to_binary(input_string):
    return ' '.join(format(ord(char), '08b') for char in input_string)

def binary_to_string(binary_string):
    binary_values = binary_string.split(' ')
    return ''.join(chr(int(bv, 2)) for bv in binary_values)


print(encrypt('ccococ', '$#kvgb'))
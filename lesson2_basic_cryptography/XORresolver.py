def xor_binary_strings(plaintext, keystream):
    """
    Performs XOR operation between two binary strings.
    Preserves spaces in the input strings.
    
    Args:
        plaintext (str): Binary string with possible spaces
        keystream (str): Binary string with possible spaces
    
    Returns:
        str: The result of XOR operation, preserving the spacing pattern
    """
    # Remove spaces to get clean binary strings
    clean_plaintext = plaintext.replace(" ", "")
    clean_keystream = keystream.replace(" ", "")
    
    # Check if the binary strings have the same length
    if len(clean_plaintext) != len(clean_keystream):
        raise ValueError("Binary strings must have the same length after removing spaces")
    
    result = []
    p_index = 0  # Index for the clean plaintext
    
    # Process each character in the original plaintext string
    for char in plaintext:
        if char == " ":
            # If it's a space, keep it as a space
            result.append(" ")
        else:
            # Get corresponding bits and perform XOR
            p_bit = int(clean_plaintext[p_index])
            k_bit = int(clean_keystream[p_index])
            xor_result = p_bit ^ k_bit  # Python's XOR operator
            result.append(str(xor_result))
            p_index += 1
    
    return "".join(result)

# Example usage for the exercise in the image
plaintext = "P = 01000110 00000110 00111110 11110011"
keystream = "R = 01000110 00000110 00111110 11110011"

# Extract just the binary parts
p_binary = plaintext.split("=")[1].strip()
r_binary = keystream.split("=")[1].strip()

# Calculate P⊕R
ciphertext = xor_binary_strings(p_binary, r_binary)
print(f"Plaintext:  {p_binary}")
print(f"Keystream:  {r_binary}")
print(f"Ciphertext: {ciphertext}")
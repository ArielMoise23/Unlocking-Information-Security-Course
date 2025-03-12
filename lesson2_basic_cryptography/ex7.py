from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    if not is_ascii(s):
        return False
    
    most_used_letters = ['e', 't', 'a', 'o', 'i', 'n']
    
    text = s.lower()  # Convert to lowercase to count 'A' and 'a' as the same
    letters_count = Counter(c for c in text if c.isalpha())  # Count only letters
    
    most_used_letters_in_text = [letters for letters, count in letters_count.most_common(3)]
    
    if not len(most_used_letters_in_text):
        return False

    for letter in most_used_letters_in_text:
        if letter not in most_used_letters:
            return False
    
    return True
    # pass # return boolean

## TESTS

is_english('12345678901234567890123456789012345678901234567890')
is_english('!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()')

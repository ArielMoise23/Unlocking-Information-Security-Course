import time
import sys # ignore
sys.path.insert(0,'.') # ignore
# from Root.pswd import real_password
real_password = '7630' # for testing (a str)

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    test_password = '0000'

    password_found = False
    while not password_found: 

        start = time.time()  # Record start time
        is_password_correct = check_password(test_password)
        end = time.time()  # Record end time

        elapsed = first_decimal_digit(end - start) - 1  # Calculate elapsed time

        if is_password_correct:
            return test_password

        if elapsed <= 3 and not is_password_correct:
            new_pass = str_to_list_of_nums(test_password)
            new_pass[elapsed] = new_pass[elapsed] + 1
            test_password = list_to_str_with_separator(new_pass)

    pass # return cracked password

def list_to_str_with_separator(lst, separator=''):
    return separator.join(map(str, lst))

def str_to_list_of_nums(s):
    return [int(char) for char in s]

def first_decimal_digit(number):
    return int(number * 10) % 10

crack_password()
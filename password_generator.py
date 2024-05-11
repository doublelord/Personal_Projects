
# check for lenght of password  (not < than 8)
# check for 1 special symbols
# check for UPPERCASE letter
# check for lowercase letter
# check for number

import random


def password_generator(length):

    symbols = '$@#%~!@^&*()+'

    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

    numbers = '1234567890'

    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    password = []

    while len(password) < 12:

        password.append(uppercase_letters[random.randint(0, 25)])
        password.append(lowercase_letters[random.randint(0, 25)])
        password.append(numbers[random.randint(0, 9)])
        password.append(symbols[random.randint(0, 12)])

    random.shuffle(password)
    return ''.join(password)


print(password_generator(7))

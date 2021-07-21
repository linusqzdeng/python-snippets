# A password generator.
# Strong passwords have a mix of lowercase letters, uppercase letters, numbers 
# and symbols.

# The password has 3 levels of strength. The highest level of password contain 16 numbers
# characters, level 2 contains 8 numbers of characters and level 1 only combines with 
# one or two simple words from a given list.

## some fixed variables
CH_LOWER = 'abcdefghijklmnopqrstuvwxyz'
CH_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = '~!@#$%^&*()-=_+[]|;:,./?<>'
SIMPLE_LIST = ['easy', 'peasy', 'password']

## function of password generator
import random

def paswrdGentor(strength=3):
    # level 3
    if strength == 3:
        seq_lowercase = random.sample(CH_LOWER, 4)
        seq_uppercase = random.sample(CH_UPPER, 4)
        seq_symbols = random.sample(SYMBOLS, 4)
        seq_numbers = [str(i) for i in (random.sample(range(0, 10), 4))]

        raw_password = seq_lowercase + seq_uppercase + seq_numbers + seq_symbols
        random.shuffle(raw_password)
        password = ''.join(raw_password)

        return password

    # level 2
    elif strength == 2:
        seq_lowercase = random.sample(CH_LOWER, 2)
        seq_uppercase = random.sample(CH_UPPER, 2)
        seq_numbers = [str(i) for i in random.sample(range(0, 10), 4)]

        raw_password = seq_lowercase + seq_uppercase + seq_numbers
        random.shuffle(raw_password)
        password = ''.join(raw_password)

        return password
    
    elif strength == 1:
        raw_password = random.sample(SIMPLE_LIST, 2)
        random.shuffle(raw_password)
        password = ''.join(raw_password)

        return password
    
    # invalid input
    else:
        error_statment = print('Invalid input. Please enter the strength level from 1 to 3')
        return error_statment

password_strength = int(input('''Tell me what level of password 
do you want (from level 1 to 3):\n'''))

print('--'*25)
print('Here is your password:\n', paswrdGentor(password_strength))
print('--'*25)
## some fixed variables
CH_LOWER = 'abcdefghijklmnopqrstuvwxyz'
CH_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = '~!@#$%^&*()-=_+[]|;:,./?<>'
SIMPLE_LIST = ['easy', 'peasy', 'password']

## function of password generator
import random

print(random.sample(CH_LOWER, 4))
print(random.sample(CH_UPPER, 4))

raw_password = random.sample(CH_UPPER, 4) + random.sample(CH_LOWER, 4)
print(raw_password)

random.shuffle(raw_password)
print(raw_password)
password = ''.join(raw_password)
print(password)


# def paswrdGentor(strength=3):
#     # level 3
#     if strength == 3:
#         seq_lowercase = random.sample(CH_LOWER, 4)
#         seq_uppercase = random.sample(CH_UPPER, 4)
#         # seq_symbols = random.sample(SYMBOLS, 4)
#         # seq_numbers = random.sample(range(0, 10), 4)

#         raw_password = seq_lowercase + seq_uppercase
#         password = ''.join(random.shuffle(raw_password))

#         return password
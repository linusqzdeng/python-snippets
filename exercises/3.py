import random

num = random.randrange(1000, 9999)
print(num)
guess = int(input('Guess what 4-digit number I have got:\n'))

list_n = list(str(num))
list_g = list(str(guess))
correct_list = list(set([x for x in list_n for y in list_g if x == y]))

print(correct_list)

# This program takes a list of numbers and makes a new list of only the first element
# and last elements of the given list. 

import random

# generate a list of numbers
num_list = random.sample(range(1, 30), 15)
new_list = []

# define a function
def list_ends(list):
    new_list.append(list[0])
    new_list.append(list[-1])

    return new_list

print(num_list)

list_ends(num_list)

print(new_list)

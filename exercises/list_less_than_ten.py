# This program prints out all the elements of the list that are less than 10.

a = [1, 1, 10, 4, 5, 7, 11, 9, 21, 24, 34, 45, 56, 74, 89]

# Outputting the result in a new list.
new_list = []

for x in a:
    if x < 10:
        new_list.append(x)
    else:
        pass

print(new_list)

# Writing this in one line.
print([y for y in a if y < 10])

'''
list comprehension: [output] for [item] in [list] if [filter]
in this example: 
[output] = y
[item] = y
[list] = a
[filter] = y < 10
'''
'''
An one line program that makes a new list that has only
the even elements of the given list.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x for x in a if x % 2 == 0])

# the same as

new_list = [y for y in a if y % 2 == 0]
print(new_list)

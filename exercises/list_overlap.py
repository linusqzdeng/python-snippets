'''
This program returns a list that contains only the elements that are common between 
the lists (without duplicates).
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set_a = set(a)
set_b = set(b)

common_elements = []

for x in set_a:
    if x in set_b and x in set_a:
        common_elements.append(x)
    else:
        pass

print(common_elements)

# another solution

c = []

for y in b:
    if y in a and y not in c:       # remove the duplicates
        c.append(y)
    else:
        pass

print(c)

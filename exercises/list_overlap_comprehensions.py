# A different solution of the exercise list overlap

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# define am empty list c
c = []

# list comprehension
result = [x for x in set(a) if x in b]

# remove the dulplicates
for y in result:
    if y in result and y not in c:
        c.append(y)
    else:
        pass

print(result)

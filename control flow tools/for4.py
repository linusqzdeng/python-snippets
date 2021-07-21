# print all the odd number
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in a:
    if x % 2 == 0:
        continue
    print(x)

# range
for x in range(1, len(a), 2):
    print (x, end = '|')

# slicing
print(a[0: len(a): 2])
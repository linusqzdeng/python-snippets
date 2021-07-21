# Using for in method to print number 1 to 10000 without storing
# the object and taking up too much RAM

def gen(max):
    n = 1
    while n < max:
        n += 1
        yield n

g = gen(10000)
for i in g:
    print(i)

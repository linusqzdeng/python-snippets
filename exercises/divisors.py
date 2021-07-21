'''
This program asks the user for a number and then print out a list of
all the divisors of that number
'''

num = int(input('Give me a numebr: '))
print([x for x in range(1, num + 1) if num % x == 0])

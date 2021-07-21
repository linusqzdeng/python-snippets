# This program asks the user for a number and determines whether the number is prime or not.
# A prime number is a number that has no divisors.

# asks for a number
print('Give me a positive integer and I will help you check whether it is a prime')

num = int(input('Number: '))

# define a function to distinguish a prime and a composite
def prime_or_composite(num):
    check_list = []     # an empty list for checking the number of divisors
    
    for x in range(1, num):
        if num <= 0:
            print('Number less than zero and zero cannot be a prime.')
            break
        elif num % x == 0:
            check_list.append(x)
        else:
            pass
    
    count_check = len(check_list)
    return count_check

print(num, 'has', prime_or_composite(num) - 1, 'divisor(s) other than 1 and itself')

if prime_or_composite(num) > 1:
    print('The given number is a composite.')
else:
    print('The given number is a prime.')

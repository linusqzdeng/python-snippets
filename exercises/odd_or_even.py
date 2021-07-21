# This program tells you whether the number you enter is even or odd.
num = int(input('Enter a number to check: '))
check = int(input('Enter a numebr ot devide by: '))

if num % 4 == 0:
    print(str(num) + ' is a nultiple of 4.')
elif num % 2 == 0:
    print(str(num) + ' is even.')
else:
    print(str(num) + ' is odd.')

# Check whether the numebr can be evenly divided by another number.
if num % check == 0:
    print(num, 'can be evenly divided by', check)
else:
    print(num, 'does not divede evenly by', check)

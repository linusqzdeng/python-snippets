# Find an even number

for n in range(2,21):
    if n % 2 == 0:
        print('found an even number', n)
    else:
        print('found a number', n)

# 'continue' statement

for x in range(2, 11):
    if x % 2 == 0:
        print('found an even number', x)
        continue
    print('found a numebr', x)
    
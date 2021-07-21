'''
Triangle quest 1:
Print out N-1 lines of integers like below:
1
22
333
4444
where N=5

note that str method cannot be used

Triangle quest 2:
print out N lines of integers like below:
1
121
12321
1234321
123454321
where N=5

use no more than two lines and str method cannot be used

constraint: 0 < N < 10
'''

for i in range(1, int(input('Enter N for Triangle Quest 1:')) + 1):
    print(i * (10**i - 1) // 9)

print('=' * 30)

for i in range(1, int(input('Enter N for Triangle Quest 2:')) + 1):
    print((1 - 10**i) ** 2 // 81)

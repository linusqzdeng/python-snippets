import re

a = 'apple, banana, orange, pineapple, pear'

r = re.findall('apple', a)
print(r)

# print(a.index('apple')>-1)
# print('apple' in a)


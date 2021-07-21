import re

s = 'ABCD76823536988751341EFOGJS'

# def subsitute(value):
#     matched = value.group()
#     if int(matched) >= 6:
#         return '9'
#     else:
#         return '6'

r = re.sub('[A-Z]', 'L', s)
print(r)

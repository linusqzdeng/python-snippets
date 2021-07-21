# def compare(x, y):
#     return True if x > 3 else False

# print(compare(2, 1))

y = 4
r = map(lambda x: x if x > y else y, [5,])
print(list(r))
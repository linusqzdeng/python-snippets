original_spot = 0

# def whereAmI(n):
#     global original_spot
#     steps = original_spot + n
#     original_spot = steps
#     return steps

# print(whereAmI(2))
# print(whereAmI(3))
# print(whereAmI(4))


def whereAmI(position):
    def w(step):
        nonlocal position
        new_position = position + step
        position = new_position
        return position
    return w


r = whereAmI(original_spot)
print(r(2))
print(r.__closure__[0].cell_contents)
print(r(3))
print(r.__closure__[0].cell_contents)
print(r(6))
print(r.__closure__[0].cell_contents)
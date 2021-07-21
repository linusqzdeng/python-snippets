from enum import Enum

class NUMBER(Enum):
    ONE = 1
    ONE_ALIAS = 1
    TWO = 2
    THREE = 3

# generally cannot print out the name of alias
for n in NUMBER:
    print(n)

# use __members__.items to show all elements under
for m in NUMBER.__members__.items():
    print(m)
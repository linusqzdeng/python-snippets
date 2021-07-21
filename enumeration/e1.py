from enum import Enum

class NUMBER(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

print(NUMBER.ONE == NUMBER.TWO)
print(NUMBER.ONE is NUMBER.TWO)
print(NUMBER['ONE'])
print(NUMBER.ONE.value)
print(NUMBER.ONE.name)
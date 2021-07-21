import m1
print(m1.a)

# use 'as' simplify the module name
import m1 as m
print(m.a)

# from ... import ...
from m1 import a 
print(a)

# use 'import *' to import all the variables
# __all__ = ['', ''] defines all the variables imported by *

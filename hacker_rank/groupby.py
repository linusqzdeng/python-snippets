"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .
You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
For a better understanding of the problem, check the explanation
"""

from itertools import groupby

# define two empty lists for storing keys
groups = []
uniquekeys = []

# define a function of compressing
def compressing_string(s):

    # for loop
    for k, g in groupby(s):
        groups.append(list(g))
        uniquekeys.append(k)


# define input string
s = input()

# run the funct¡ion
compressing_string(s)
print(groups)
print(uniquekeys)

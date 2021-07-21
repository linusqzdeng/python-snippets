# -*- coding: UTF-8 -*-

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.

# for each element in set A, yout gain 1 happiness
# while for each element in set B, you lose 1 happiness


n, m = int(input().split())    # define the number of integers n and integer m within each set

input_int = [input() for _ in range(n)]     # generate the list of integers

set_a = {input() for _ in range(m)}     # define set A
set_b = {input() for _ in range(m)}     # define set B


def happiness(a, b, n):
    happy = 0
    unhappy = 0     # define the origin score of happiness

    for i in a:
        if i in n:
            happy += 1

    for j in b:
        if j in n:
            unhappy -= 1

    return happy + unhappy


happiness(set_a, set_b, n)

'''
You are given a spreadsheet that contains a list of N athletes and
their details (such as age, height, weight and so on).
You are required to sort the data based on the Kth attribute and
print the final resulting table. Follow the example given below for better understanding.

e.g.
input:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''

import pandas as pd

n, m = input().split()     # define N and M

arr = []    # empty list for storing athlete inputs

for _ in range(int(n)):
    arr.append(list(map(int, input().rstrip().split())))    # receive inputs

k = int(input('Enter which attribute you want to sort with:'))      # define the attribute index

df = pd.DataFrame(
    arr, columns=["attribute_{}".format(i) for i in range(int(m))]
)

df = df.sort_values(by=[df.columns[k]], axis=0)

print(arr)
print(df)

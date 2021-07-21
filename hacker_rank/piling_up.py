# Stacking up the cubes where the length upper cube is always smaller than
# the length of the bottom one. Also cubes can only be picked up from the
# left-most or right-most of the list. Finally print out the result "yes or no"
# depending on the pile can be stacked up or not

# The first line contains a single integer , the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains , the number of cubes.
# The second line contains  space separated integers, denoting the sideLengths
# of each cube in that order.

from collections import deque

for _ in range(int(input("How many test you want to run: "))):

    block_size = int(input("Size of the blocks: "))
    blocks = list(map(int, input().rstrip().split()))

    while len(blocks) > 0:

        max_num = max(blocks)
        max_num_index = blocks.index(max_num)

        if (max_num_index == 0) or (max_num_index == len(blocks) - 1):
            blocks.remove(max_num)
            continue
        else:
            print('No')
            break

    if len(blocks) == 0:
        print('Yes')

# ==================================================================== #
for _ in range(int(input("How many test you want to run: "))):

    size, blocks = input("Size of the blocks: "), deque(map(int, input().rstrip().split()))
    for cube in sorted(blocks, reverse=True):
        if blocks[0] == cube:
            blocks.popleft()
        elif blocks[-1] == cube:
            blocks.pop()
        else:
            print('No')
            break
    else:
        print('Yes')

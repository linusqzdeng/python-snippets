# Build a functions that achieve the below outcome
# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3
# Output
# AB
# CA
# AD

sting, k = input(), int(input())


def merge_the_tools(strings, k):

    n_chunk = [strings[i:i + k] for i in range(0, len(strings), k)]
    count = 0

    while count < len(n_chunk):

        for element in n_chunk:

            duplicate = ''

            for i in element:
                if i not in duplicate:
                    duplicate += str(i)

            count += 1
            print(duplicate)
            


result = merge_the_tools('AABCAAADA', 3)

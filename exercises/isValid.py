'''Check if the parentheses in the string are paired'''

def isValid(s:str):
    pairs = {'(': ')', '[': ']', '{': '}'}
    check = []

    for x in s:
        if x in pairs:
            check.append(x)
        elif len(check) == 0 or pairs[check.pop()] != x:
            return False
    return len(check) == 0

print(isValid('(]'))

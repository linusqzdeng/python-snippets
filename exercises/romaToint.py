'''Convert Roma numerals in to integer number'''

def romaToint(s: str):
    # define the values of roma numerals
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result, store = 0, 0
    for i in s[::-1]:
        if symbols[i] >= store:
            result += symbols[i]
        else:
            result -= symbols[i]
        store = symbols[i]
    return result

print(romaToint('II'))

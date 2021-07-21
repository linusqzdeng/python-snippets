''' Return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.'''

def strStr(haystack: str, needle: str):
    if 0 <= len(haystack) and len(needle) <= 5 * (10 ** 4):

        # if neddle is an empty string
        if needle == '':
            return 0
        
        # wether the haystock contains the needle
        if needle in haystack:
            str_index = haystack.index(needle)
        else:
            str_index = -1

    else:
        return 'The string length is too long!'
    
    return str_index

test = strStr('hello', '')
print(test)
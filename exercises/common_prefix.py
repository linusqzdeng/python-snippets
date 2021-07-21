'''Find the common prefix among a list of strings'''

def longestCommonPrefix(strs: list):
        
    # find the minimised string length
    length_list = [len(l) for l in strs]
    min_len = min(length_list)
    
    # extract the prefix of each of the string
    count = 0
    while count <= min_len:
        test_list = [x[0:count] for x in strs]
        if len(set(test_list)) == 1:
            count += 1
            prefix_list = test_list
        else:
            break

    # see whether all of th prefix are in common
    if len(prefix_list) >= 1:
        return prefix_list[0]
    else:
        return 'a'

print(longestCommonPrefix(['gompare', 'company', 'complain']))

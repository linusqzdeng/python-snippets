# This program takes a list and returns a new list that contains all the elements of
# the first list minus all the duplicates.

a = [1, 1, 3, 5, 7, 4, 3, 6, 5, 8, 8, 13, 24, 33, 12, 13, 17, 14]

def remove_duplicates(list):
    new_list = []
    for x in a:
        if x not in new_list:
            new_list.append(x)
        else:
            pass
    
    return new_list

print(remove_duplicates(a))

print('-' * 45)

# another way using sets

a = [1, 1, 3, 5, 7, 4, 3, 6, 5, 8, 8, 13, 24, 33, 12, 13, 17, 14]

def remove_duplicates_bysets(alist):
    return list(set(alist))

print(remove_duplicates_bysets(a))

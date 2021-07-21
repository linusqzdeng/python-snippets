'''Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index
where it would be if it were inserted in order.'''

def searchInsert(nums: list, target: int):
    
    ## distinct nums values
    sortnums = list(set(nums))
    target_index = 0

    ## see whether the target is in the nums
    if target in nums:
        target_index = sortnums.index(target)
    else:
        sortnums.append(target)
        sortnums = list(set(sortnums))
        target_index = sortnums.index(target)
    
    return target_index

test = searchInsert([2,2,3,4,1,23], 5)
print(test)
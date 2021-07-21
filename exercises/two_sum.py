''' Given an array of nums and an integer target, return the indices 
    of nums that add up to the target. Assume that there is only one solution.
    and the same element cannot be used twice. '''

nums = [2, 7, 11, 15]
target = 13

def two_sum(nums, target):
    n = len(nums)
    hash_table = {}
    for a in range(n):
        complement = target - nums[a]
        if complement not in hash_table:
            hash_table[nums[a]] = a
        else:
            return [hash_table[complement], a]

print(two_sum(nums, target))
'''
    Assume we are dealing with an environment that could only 
    store integers within the 32-bit signed integer range: [−231,  231 − 1].
    For the purpose of this problem,assume that your function returns 0 
    when the reversed integer overflows.
'''

num = 1234

def reverse_int(num):
    num_str = str(num) # turn num into a str
    reverse_str = num_str[::-1] # reverse the sequence of the num
    result = int(reverse_str) # turn the str back to the int
    return result

print(reverse_int(num))
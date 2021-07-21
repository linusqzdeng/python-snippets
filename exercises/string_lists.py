'''Thsi program asks the user for a string and print out whether this string is a 
palindrome or not (a palindrome is a string that reads the same forwards and backwards)
'''

# ask for a word
something = input('Give me a word: ')

# convert the given word into a list
original_list = list(something)
print(original_list)

# check if the word is a palindrome or not
check_list = original_list[::-1]

if check_list == original_list:
    print('This word is a palindrome')
else:
    print('This word is not a palindrome')

# loop solution
print('-'*40)

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-i-1]
        return x

word = input('Give me another word: ')
x = reverse(word)
print(x)
if x == word:
    print('This word is a palindrome')
else:
    print('This word is NOT a palindrome')

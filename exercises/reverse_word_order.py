# This program ask you for a string with multiple words and prints back to
# you with the same string, except with the words in backwards order.

# use split() to divide the given sentence into a list of strings
# ','.join can combine multiple strings
def back_words(something):
    
    words_list = something.split()
    backward_list = words_list[::-1]
    join_string = ' '.join(backward_list)

    return join_string

# ask for a sentence
words = input('Give me some words: ')

print(back_words(words))

# simplest solution
# def reverseWord(w):
#     return ' '.join(w.split()[::-1])

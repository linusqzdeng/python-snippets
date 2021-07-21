# define a function

def add(x, y):
    res = x + y
    return res

def word(sentence):
    print(sentence)
    return sentence

add(1, 5)
word('linus is coding')

a = add(1, 5)
b = word('linus is coding and thinking')
print(a, b, sep = '|')

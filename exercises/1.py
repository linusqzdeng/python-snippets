name = 'linus'

def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
        return x

x = reverse(name)
print(x)

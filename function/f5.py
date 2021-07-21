# 变量的作用域

c = 20

def add(a, b):
    c = a + b
    print(c)

add(1, 2)       # 3
print(c)        # 20

# variables defined within a function would not
# affect variables outside the function
# However, global variables can be called within the function

# global keyword
def demo():
    global c
    c = 21

demo()
print(c)

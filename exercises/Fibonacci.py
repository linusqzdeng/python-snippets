# This program asks the user how many Fibonacci numbers to generate and generates them.

n = 400


def fib(n):
    fib = []
    a, b = 0, 1

    loop_count = 0

    if n <= 0:
        fib = [0]
    else:
        while True:
            fib.append(b)
            a, b = b, a + b
            loop_count += 1

            if loop_count == n:
                break
            else:
                pass

    return fib


print(fib(n))

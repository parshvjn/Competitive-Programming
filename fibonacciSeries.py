#In fibonacci sequence, the 3rd number is the addition of previous 2 numebrs.
# ex --- 0 1 1 2 3 5 8 13 21 34

def fib(a):
    if a <= 1:
        return a
    else:
        return (fib(a-1) + fib(a-2))


for i in range(10):
    print(fib(i), end = ' ')
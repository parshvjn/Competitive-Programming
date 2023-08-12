#method 1: reccursive
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

#method 2: iterative

def factorial1(n):
    a = 1
    for i in range(1,n+1):
        a*=i
    return a
    
print(factorial1(10))

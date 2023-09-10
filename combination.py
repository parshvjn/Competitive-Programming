from itertools import permutations,combinations
from factorial import *

a = [i for i in combinations('abc', 1)]

def combination(string, r):
    n = len(string)
    if r<=n:
        a = factorial(n)/(factorial(n-r)*factorial(r))
        return a

print(combination('yes', 2))


def combo(lst,r):
    if r==0:
        return [[]]
    li= []
    for i in range(0,len(lst)):
        m = lst[i]
        rem = lst[i+1:]
        mn = combo(rem,r-1)
        for j in mn:
            li.append([m,*j])
    return li

print(combo(list("abc"), 2))
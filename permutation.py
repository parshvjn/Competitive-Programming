from itertools import permutations,combinations
from factorial import *

# using built-in function
l = [i for i in permutations('abc')]
# print(l)

##########################################
def permutation(string, r):
    n = len(string)
    if r<=n:
        a = factorial(n)/factorial(n-r)
        return a

print(permutation('yes',2))

def permute(String,i=0):
    if i==len(String):
        print("".join(String))

    for j in range(i,len(String)):
        words = list(String)
        words[i],words[j] = words[j],words[i] # swap
        permute(words,i+1)

 
permute('yes')
###########################################
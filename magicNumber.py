#Hw: write magic number code in iterative way(in a function)

def magic_number(num):
    while num >= 10:
        l = str(num)
        a = sum(int(i) for i in l)
        num = a
    return num == 1

a = 1729

if magic_number(a):
    print('magic number')
else:
    print('not magic number')

#reference:
# a=1729

# l=list(str(a))

# a=list(str(sum([int(i) for i in l])))

# a = sum(int(i) for i in a)

# a = list(str(a))

# print('magic number') if sum(int(i) for i in a)==1 else print('not a magic number')
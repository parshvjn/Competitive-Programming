#pythonic way:
a = [1,6,8,4,8,4,3,567]
# print(a.count(4))
a.sort()
c=[]
for item in a:
    b = a.count(item)
    if b>1:
        c.append(item)

print(list(set(c)))

############################
#Hw: write this in list comprehension for both (above and below)(conventional and pythonic)

# ABOVE:python (in list comprehension)

a = [1,6,8,4,8,4,3,567]
a.sort()
c = list(set([item for item in a if a.count(item)>1]))
print(c)

# BELOW:conventional (in list comprehension)

d = [5,4,2,30,49,6,2,3,4]
u=[]
u = [d[j] for i in range(0,len(d)) for j in range(i+1, len(d)) if d[i] == d[j] and d[i] not in u]
print(u)

############################
#conventional way:

d = [5,4,2,30,49,6,2,3,4]
u=[]
for i in range(0, len(d)):
    for j in range(i+1, len(d)):
        if d[i]==d[j] and d[i] not in u:
            u.append(d[i])
            print(d[j])


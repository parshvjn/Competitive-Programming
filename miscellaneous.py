# Building of dictionary using 2 lists

# print(ord("A"))

# print(chr(65))

# a = list(range(0,12))
# b = [chr(item) for item in range(0,128)]
a = list(range(0,128))
b = [chr(item) for item in a]
# print(b)

# print(dict(zip(b,a)))

# print(set(zip(b,a)))
# print(list(zip(b,a)))

# .......................................................CONVENTIONAL WAY......................................................................
c = {}
index = 0
for item in a:
    c[index] = b[index]
    index += 1

# print(c)

# .....................................................ENUMERATE FUNCTION.........................................................................

c2 = {}
for i, j in enumerate(b):
    c2[j] = i

# print(c2)

# ...................................................DICTIONARY COMPREHENSION...........................................................................

g = {key:value for key, value in enumerate(b)}
# print(g)

# g = {key:value for key, value in zip(b,a)}
# print(g)

# ...................................................PACKING AND UNPACKING OF DICTIOANRIES...........................................................................

t = {"r":1, "t":8}
u = {"y":89, "g":234}
v = {"h":34, "j":35}

y = {**v,**t,**u}
print(y)

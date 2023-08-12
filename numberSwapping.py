a=10
b=20

# SWAPPING OF 2 VARIABLES (using 3rd variable temp)------
temp = a
a = b
b = temp


print(a,b)

#------------------SWAPPING OF 2 VARIABLES WITHOUT USING 3RD VARIABLE

a = a + b #a = 30
b = a-b   #b = 10
a = a-b   #a = 20
print(a,b)

#------------------

#python supports multiple variable assignment in a single line.
# a,b = 10,20
# print('multiple assignment', a,b)

b,a = a,b
print(a,b)
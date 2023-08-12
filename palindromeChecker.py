#method 1: trick
a = 1221
# print(a==a[::-1])

#method 2: conventional way (only for digits)
n = int(input('enter number: '))
temp = n #original number
reverse = 0
while n>0:
    ones = n%10#getting the ones place value
    reverse = reverse*10 + ones # adds the next ones place at the right of the reverse variable
    n = n // 10 #removes the ones place from n(original input)

# print(reverse)
if temp == reverse:
    print('palindrome')
else:
    print('not palindrome')
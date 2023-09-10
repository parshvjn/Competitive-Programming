# #1
def resultrank(array):
    a = array.copy()
    a.sort()
    d = {}

    counter = 1
    for e in a:
        if e not in d:
            d[e] = counter
            counter += 1
    
    new = [d[e] for e in array]
    return new

array = [100, 200, 70, 12, 90]
# print(resultrank(array))

#4

def match(s1, s2):
    indexes = []
    for co,va in enumerate(s1):
        if va == "*":
            indexes.append(co)
    s1 = s1.replace("*", "")
    s2 = list(s2)

    for index in indexes:
        # print(s2[index])
        s2[index] = ''
    s2 = "".join(s2)
    
    # print(s1, '-->', s2)
    return s1 == s2

s1 = 'vista int*llig*nce'
s2 = 'vista intelligence'

print(match(s1,s2))

#6

def maximum(arr):
    if len(arr) != 0:
        max1, a = arr[0], arr[0]

        for x in arr[1:]:
            a = max(x, a + x)
            max1 = max(max1, a)

    return max1

arr = [-7, -8, -1, -5, -4, -3]
# print(maximum(arr))

#7

def reverseString(i:str):   
    li=i.split(' ')
    f=[]
    if len(i) >=1:
        for word in li:
            b = list(word)
            d=[]
            for x in range(len(word)-1, -1, -1):
                d.append(b[x])
            
            e = ''.join(d)
            f.append(e)
        g=' '.join(f)
        return g
    else:
        return None
    

if '__main__()':
    a = reverseString('Today is a wonderful day')
    # print(a)


#8

# :|

arr1 = [1,'m',2,'b','x',0,5,'a',4,'z']
alph = []
digit = []

for e in arr1:
    if str(e).isalpha():
        alph.append(e)
        
    else:
        digit.append(e)

digit = sorted(digit, reverse=True)
alph = sorted(alph)
# print(digit+alph)
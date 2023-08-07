# CONSTRAINTS
# length(string)>=1

# a = ['34', 'fg', '45']
# b=' a '.join(a)
# print(b)

def stringReversal(i:str):   
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
    a = stringReversal('welcome to pluto')
    print(a)


# HW: reverse the string keeping the original position same
# for ex:
# in: 'welcome to pluto'
# out: 'emoclew ot otulp

# input= 'welcome to pluto'
# print(input.split(' '))

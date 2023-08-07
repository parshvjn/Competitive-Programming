# parshv is a grade 8 student and is curious to know about the  different types of mirrors. in school he has studied that whatever object is placed in front of a mirror it gets reversed. parshv does a small experiment to see what if the words are placed in fron of the mirrors.
# he observed that whatever he wrote on the paper it got reveresed. whethere it is a sentence or a word. also he observed that whitespace is also maintained. following this scenario he tries to write the code which can yeild the same mirror image results for different sets of string.

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
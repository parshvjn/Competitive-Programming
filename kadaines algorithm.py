
def old_kadaines(array,size):
    op=[]
    max_start = array[0]
    max_end   = 0
    for i in range(0,size):
        max_end = max_end + array[i]
        if max_end < 0 :
            max_end = 0
        elif (max_start<max_end):
            op.append(array[i])
            max_start = max_end
    return max_start, op



def modified_kadaines(array,size): 
    op=[]
    max_start = array[0]
    max_end   = 0
    for i in range(0,size):
        max_end = max_end + array[i]
        if (max_start<max_end):
            op.append(array[i])
            max_start = max_end
        if max_end < 0 :
            max_end = 0
        
    return max_start, op




li=[-2,-3,4,-1,2,3,5,-3]
Sum,pp=modified_kadaines(li,len(li))





li=[-3,-4,-9,-1,-2,-3,-5,-3]
ss,pp=old_kadaines(li,len(li))




li=[-3,-4,-9,-1,-2,-3,-5,-3]
ss,pp=modified_kadaines(li,len(li))








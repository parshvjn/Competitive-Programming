def linearSearch(li:list, fn): #fn : finding number
    for x,y in enumerate(li):
        if y == fn:
            return f"found at index {x}"
    else:
        return 'Not found'

# print(linearSearch([1,5,5,3,7], 7))


def binarySearch(li:list, fn, start,end):
    li.sort()
    start, end = 0, len(li)-1
    mid = (start+end)//2
    if start <= end:
        if fn == li[mid]:
            return f"Found at {mid}"
        elif fn > li[mid]:
            start,end = mid+1,len(li)
            return binarySearch(li[mid+1:len(li)], fn, start, end)
        elif fn < li[mid]:
            start,end = 0, mid
            return binarySearch(li[0:end], fn, start, end)
    else:
        return "Not found"

li = [1,2,5,3,6,4]
print(binarySearch(li, 45,0,len(li)))

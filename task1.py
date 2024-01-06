inputFile=open('input1.txt','r')
f_line=int(inputFile.readline())
list1=list(map(int,inputFile.readline().split(' ')))
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half=arr[mid:]
        a1 = mergeSort(left_half)
        a2 = mergeSort(right_half)
        return merge(a1, a2)
def merge(a1, a2):
    out=[]
    i = j  = 0
    # Merge the two halves back together in sorted order
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            out.append(a1[i])
            i += 1
        else:
            out.append(a2[j])
            j += 1
    # Check if any elements were left in the left half
    while i < len(a1):
        out.append(a1[i])
        i += 1
    # Check if any elements were left in the right half
    while j < len(a2):
        out.append(a2[j])
        j += 1
    return out
out=mergeSort(list1)
outputFile = open('output1.txt', 'w')
outputFile.writelines(' '.join(map(str, out)))
inputFile.close()
outputFile.close()
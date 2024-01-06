inputFile=open('input3.txt','r')
f_line=int(inputFile.readline())
list1=list(map(int,inputFile.readline().split(' ')))
count=0
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half=arr[mid:]
        a1 = mergeSort(left_half)
        a2 = mergeSort(right_half)
        return count_inversions(a1, a2)
def count_inversions(a1, a2):
    global count
    out=[]
    i=j=k=0
    # Merge the two halves back together in sorted order
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            out.append(a1[i])
            i += 1
        else:
            out.append(a2[j])
            j += 1
            count+=len(a1[i:])  #Counting the possible inversions
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
outputFile = open('output3.txt', 'w')
outputFile.writelines(str(count))
inputFile.close()
outputFile.close()
inputFile=open('input2.txt','r')
N=int(inputFile.readline())
list1=list(map(int,inputFile.readline().split(' ')))
def mergeSort(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half=arr[mid:]
        a1 = mergeSort(left_half)
        a2 = mergeSort(right_half)
        return Find_Max(a1, a2)
def Find_Max(a1,a2):
    if a1>a2:
        return a1
    else:
        return a2
out=mergeSort(list1)
outputFile=open('output2.txt','w')
outputFile.writelines(str(out))
inputFile.close()
outputFile.close()

#Time complexity of this code is O(nlogn).

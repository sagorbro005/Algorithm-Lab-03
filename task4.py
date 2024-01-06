inputFile=open('input4.txt','r')
n=int(inputFile.readline())
list1=list(map(int,inputFile.readline().split(' ')))
def max_square(a1, a2):
        if a1**2 > a2**2:
            return a1
        else:
            return a2
def mergeSort(arr):
        if len(arr)==0:
          return 0
        if len(arr) <= 1:
            return arr[0]
        else:
            mid = len(arr) // 2
            a1 = mergeSort(arr[:mid])
            a2 = mergeSort(arr[mid:])
            return max_square(a1, a2)
maxi=float('-inf')
for k in range(len(list1)):
    out=list1[k]+ (mergeSort(list1[k+1:]))**2
    if out>maxi:
        maxi=out
outputFile=open('output4.txt','w')
outputFile.writelines(str(maxi))
inputFile.close()
outputFile.close()
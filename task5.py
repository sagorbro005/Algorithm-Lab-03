inputFile=open('input5.txt','r')
n=int(inputFile.readline())
arr=list(map(int,inputFile.readline().split(' ')))
def quicksort(arr,lb,ub):
    if lb<ub:
        loc=partition(arr,lb,ub)
        quicksort(arr,lb,loc-1)
        quicksort(arr,loc+1,ub)
def partition(arr,lb,ub):
    pivot=arr[lb]
    start=lb
    end=ub
    while start<end:
        while arr[start]<=pivot and start<ub:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[lb],arr[end]=arr[end],arr[lb]
    return end
quicksort(arr,0,n-1)
outputFile=open('output5.txt','w')
outputFile.writelines(' '.join(map(str,arr)))
inputFile.close()
outputFile.close()
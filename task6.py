inputFile=open('input6.txt','r')
n=int(inputFile.readline())
arr=list(map(int,inputFile.readline().split(' ')))
queries=int(inputFile.readline())
out=[]
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
def quick_select(arr,k):
    lb=0
    ub=len(arr)-1
    while True:
        loc=partition(arr,lb,ub)
        if loc==k-1:
            return arr[loc]
        elif loc<k-1:
            lb=loc+1
        else:
            ub=loc-1
for i in range(queries):
    out.append(quick_select(arr,int(inputFile.readline())))
outputFile=open('output6.txt','w')
for i in out:
    outputFile.writelines(f'{str(i)}\n')
inputFile.close()
outputFile.close()
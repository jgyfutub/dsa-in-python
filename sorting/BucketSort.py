import math
from InsertionSort import insertionSort

def BucketSort(customList):
    numberOfBuckets=round(math.sqrt(len(customList)))
    maxVAlue=max(customList)
    arr=[]
    for i in range(numberOfBuckets):
        arr.append([])
    for j in customList:
        index_b=math.ceil(j*numberOfBuckets/maxVAlue)
        arr[index_b-1].append(j)

    for i in range(numberOfBuckets):
        arr[i]=insertionSort(arr[i])

    k=0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k]=arr[i][j]
            k+=1

    return customList
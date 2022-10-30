arr=[7,9,4,8,3,6,2,1,5]
def partition(arr,pivot):
    i=0
    j=0
    while i<len(arr):
        if(arr[i]<=pivot):
            (arr[i],arr[j])=(arr[j],arr[i])
            j=j+1
        i=i+1
    for i in range(len(arr)):
        print(arr[i], end = " ")
partition(arr, arr[len(arr)-1])



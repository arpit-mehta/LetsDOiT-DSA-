    def quickSort(self,arr,low,high):
        if (low<high):
            #get pivot index
            pivotIndex=partition(arr,low,high) 
            #left half
            quickSort(arr,low,pivotIndex-1)
            #right half
            quickSort(arr,pivotIndex+1,high)
     
    #partition array and return the pivot index so that we can perform quickSort on remaining left and right halves
    def partition(self,arr,low,high):
        pivot=arr[high]
        pIndex=low
        for i in range(low,high):
            if(arr[i]<=pivot):
                arr[i],arr[pIndex]=arr[pIndex],arr[i]
                pIndex=pIndex+1
        arr[pIndex],arr[high]=arr[high],arr[pIndex]
        return pIndex

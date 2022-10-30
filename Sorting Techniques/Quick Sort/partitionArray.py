def partition(self,arr,low,high):
        #last element as pivot element
        pivot=arr[high] 
        
        #assume pivotIndex to be low initially
        pIndex=low  
        
        #run the loop from low to high 
        for i in range(low,high): 
            #current element at i less than equal to pivot 
            if(arr[i]<=pivot):
                #swap element at pIndex and i
                arr[i],arr[pIndex]=arr[pIndex],arr[i]
                #increment pIndex 
                pIndex=pIndex+1
            
        #once the loop over we need to swap our pIndex element and element at high
        arr[pIndex],arr[high]=arr[high],arr[pIndex]
        #pIndex has index of pivot 
        return pIndex
    
    
    
    
    #all elements less than pivot are to left of pIndex 
    # 0 to pIndex-1 has elements less than pIndex
    # pIndex has index of pivot 
    # pIndex+1 to high has elements greater than pIndex

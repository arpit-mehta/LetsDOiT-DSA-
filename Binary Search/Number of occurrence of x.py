def count(self,arr, n, x):
		# code here
		start = 0
		end=n-1
		firstOccurence=-1
		
		while start<=end:
		    mid=((start+end)//2)
		    
		    if arr[mid]==x:
		        firstOccurence=mid
		        end=mid-1
		    elif arr[mid]<x:
		        start=mid+1
		    else:
		        end=mid-1
		
		start = 0
		end=n-1
		lastOccurence=-1
		
		while start<=end:
		    mid=((start+end)//2)
		    
		    if arr[mid]==x:
		        lastOccurence=mid
		        start=mid+1
		    elif arr[mid]<x:
		        start=mid+1
		    else:
		        end=mid-1
	    if firstOccurence>-1 and lastOccurence>-1:      #if the element is present 
		    return lastOccurence-firstOccurence+1
		else:                                             #if the element we are searching for is not present
		    return 0

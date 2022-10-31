def binarysearch(arr, n, k):
		start=0
		end=n-1
    
    #this gives the index of the k element we are searching for.
		ans=-1;
		
    while start<=end:
		    mid=((start+end)//2)
		    
		    if arr[mid]==k:
		        ans=mid
		        return ans
		    elif arr[mid]<k:
		        start=mid+1
		    else:
		        end=mid-1
    return ans

def find(arr,n,x):
    # code here
    start=0
    end=n-1
    ansarray=[]
    ans=-1
    while start<=end:
	    
        mid=((start+end)//2)
        if arr[mid]==x:
            ans=mid       #this can be my answer,i.e, first occurence if no x is present to its left
            end=mid-1     #first occurence can be to the left of the element at mid
        elif arr[mid]<x:
            start=mid+1
        else:
            end=mid-1
    ansarray.append(ans)
    
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==x:
            ans=mid       #this can be my answer ,i.e, last occurence if no x is present to its right
            start=mid+1   #last occurence can be to the right of the element at mid
        elif arr[mid]<x:
            start=mid+1
        else:
            end=mid-1
    ansarray.append(ans)
    return ansarray

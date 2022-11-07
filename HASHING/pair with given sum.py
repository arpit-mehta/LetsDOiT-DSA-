#hashing 
def sumExists(arr, N, sum):
    #Your code here
    ans=dict()
    visited=[]
    counter=0
    for i in range(len(arr)):
        if sum-arr[i] not in ans:
            ans[arr[i]]=1
        else:
            return 1
    return 0
  #O(n) space and time
  
  
# Can also be done using 2 pointer (first sort and then for every pair from start and end see the sum and adjust the pointers accordingly)
#O(logn+n) space and time

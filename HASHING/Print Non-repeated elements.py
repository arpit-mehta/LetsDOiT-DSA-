#brute force
    #Complete this function
    #Function to return non-repeated elements in the array.
    def printNonRepeated(self,arr,n):
        ans=[]
        
        for i in range(len(arr)):
            flag=0
            for j in range(len(arr)):
                if i!=j and arr[i]==arr[j]:
                    flag=1
                    break
            if flag==0:
                ans.append(arr[i])
        return ans
        
#using dictionary
def printNonRepeated(self,arr,n):
  
        ans=dict() 
        ansarray=[]
        for i in range(len(arr)):
            if arr[i] in ans:
                ans[arr[i]]+=1
            else:
                ans[arr[i]]=1
        for i in range(len(arr)):
            if ans[arr[i]]==1:
                ansarray.append(arr[i])   
        return ansarray

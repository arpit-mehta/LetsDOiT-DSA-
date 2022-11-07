#link https://leetcode.com/problems/top-k-frequent-elements/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict=dict()
        for i in range(len(nums)):
            if nums[i] in myDict:
                myDict[nums[i]]+=1
            else:
                myDict[nums[i]]=1
        
        new=dict(sorted(myDict.items(),key=lambda item: item[1], reverse=True))
        ans=[]
        for key in new.keys():
            ans.append(key)
        
        
        return ans[:k]   
       
        
        #O(nlogn) -> due to sort
        # will optimize once i do heap (Most Optimized)

def findMin(self, nums: List[int]) -> int:
        
        n=len(nums)
        start=0
        end=n-1
        
        if nums[start]<=nums[end]:
            return nums[start]
        
        while start<=end:
            mid=((start+end)//2)
            
            if nums[mid]>nums[mid+1]:  
                return nums[mid+1]
            elif nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[start]<=nums[mid]:
                start=mid+1
            else:
                end=mid-1

  #observations
  # the array can be divided into two sorted arrays
  # Array 1 : if its the mid and it is larger then its next element then next element is surely the first and minimum element of second array
  # Array 2 : if it is the mid and it is smaller then its prev element then it is surely the smallest element
  # compare mid element with first to decide which side we need to move

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        //Selection Sort
        //O(n^2) 
        //Not Stable and Not adaptive algorithm
        
        int n=nums.size();
        
        //for the passes/runs (n elements (n-1) passes)
        for(int i=0;i<n-1;i++) 
        {
            int k=i;
            //to traverse the remaining unsorted array
            for(int j=i;j<n;j++){
                if(nums[j]<nums[k]){
                    //k points to smallest element j has seen
                    k=j;    
                }
            }
            swap(nums[k],nums[i]);
        }
        return nums;
    }
};

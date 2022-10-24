class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        //Bubble Sort
        //O(n^2) worst case
        //O(n) if already sorted
        //Stable and adaptive algorithm
        
        int n= nums.size();
        
        //for the passes/runs
        for(int i=0;i<n-1;i++) 
        {
            //to check if swaps are done or not 
            int swaps=false;
            
            //for comparisons (n-1-i because after each pass the number of comparisons will decrease)
            for(int j=0;j<n-1-i;j++){ 
                if(nums[j]>nums[j+1]){
                    swap(nums[j],nums[j+1]);
                    swaps=true; //swap has been done
                }
            }
            
            //check after each pass if no swap done that means array is sorted
            if(swaps==false){
                break;
            }
        }
        return nums;
    }
};

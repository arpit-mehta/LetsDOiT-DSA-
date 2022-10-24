class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        //Insertion Sort
        //O(n^2) worst case
        //O(n) if already sorted
        //Stable and adaptive algorithm
        
        int n=nums.size();
        
        //for the passes/runs (n elements (n-1) passes)
        for(int i=1;i<n;i++) 
        {
            int j=i-1; //start comparing from here with element to be inserted
            int x=nums[i]; //the element that has to be inserted
            
            //loop through all elements and compare with element to be inserted
            //loop from n-1 to j>-1 
            //&& loop till you fing element less than element to be inserted
            while(j>-1 && nums[j]>x){
                nums[j+1]=nums[j];
                j--;
            }
            nums[j+1]=x;
        }
        return nums;
    }
};

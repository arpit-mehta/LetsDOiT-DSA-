class Solution
{
    public:
    //Function to sort an array using quick sort algorithm.
    void quickSort(int nums[], int start, int end)
    {
        if(start<end){ //start must always be less than end 
            int pIndex=partition(nums,start,end); //this will give the index of the pivot element
            quickSort(nums,start,pIndex-1); //sort the array from 0 to that pivot index-1
            quickSort(nums,pIndex+1,end);   //sort the array from pivot index + 1 to the last element
        }
    }
    
    public:
    //helps for teh partitioning of the array 
    //returns the final index of the pivot element
    int partition (int nums[], int start, int end)
    {
       int pivot=nums[end];//pivot will always be last index
        int pIndex=start; //set partition index to start inititally
        
        //traverse the list from start to pivot
        for(int i=start;i<end;i++){ 
            if(nums[i]<=pivot){  //all element less than equal to pivot on one side 
                swap(nums[i],nums[pIndex]);
                pIndex++;
            }
        }
        //swap the pivot element and the element at pIndex 
        swap(nums[pIndex],nums[end]);  
        return pIndex; //return the index of the pivot index
    }
};

bool isPowerofTwo(long long n){
        
       if((n & (n-1))!=0 || n==0){     //if n&(n-1) != 0 in this case return false also if n==0
            return false;
        }
        else{
           return true; 
        }  
        
    }
//power of 2 means 1 at most Significant bit and rest all 0
//so when we do AND of power of 2 and and 1 number less than power of 2 we always get 0 as our answer. 

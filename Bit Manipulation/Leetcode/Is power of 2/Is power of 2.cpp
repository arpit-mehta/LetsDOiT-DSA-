//Link - >   https://leetcode.com/problems/power-of-two/submissions/

bool isPowerOfTwo(int n) {
        if(n<=0){
            return false;
        }
        else{
            return ((n&(n-1))==0);
        }
    }

//link- 

//TLE Solution
int countSetBits(int n)
    {
        int count=0;
        for(int num=1 ; num<=n ; num++)  //looping through each number
        {
            for(int bit=0 ; bit<=ceil(log2(n)) ; bit++) //looping through each bit of the number 
            {
                if((num & (1<<bit))!=0){    //if num & 1 for current bit != 0 that means it is set so increase the counter.
                    count++;
                }
            }
        }
        return count;
    }
// in this we loop through each number and for that number we check number of set bits.
//O(N * logN) solution


//Optimized approach  (gives TLE)
//O(n)
// ex-> n=5 -> 101 now,
//  n/2 = 2 -> 10  we see when we divide an odd number by 2 the least significant bit is lost so number of set bits is 1 less than n.

// n=6 -> 110 now,
// n/2 = 3 -> 011 we see when we divide an even number by 2 the least significant bit is already 0 so number of set bits remain same.

//we can store for each number in an array(arr) and add 1 to number of bits at arr[n/2] if it odd 
//else remain same as arr[n/2] if even.

int countSetBits(int n)
    {
        vector<int> v(n+1,0);
        
        for(int i=1;i<=n;i++){      //going through each array element 
            if(i%2==0){             // if even then same
                v[i]=v[i/2];
            }
            else{                 //else add 1 to the bits of v[i/2]
                v[i]=v[i/2]+1;
            }
        }
      int ans=0;
        for(int i=1;i<=n;i++){  //adding all the array elements to get total set bits till n
            ans+=v[i];
        }
        return ans;
    }

//More Optimized approach  O(log n)


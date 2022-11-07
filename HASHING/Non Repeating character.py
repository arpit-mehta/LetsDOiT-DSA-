#Brute Force
def nonrepeatingCharacter(self,s):
        #code here
        ans=""
        
        for i in range(len(s)):
            flag=0
            for j in range(len(s)):
                if i!=j and s[i]==s[j]:
                    flag=1
                    break
            if flag==0:
                ans=s[i]
                break
        return ans
      
  
  #using hashing
  def nonrepeatingCharacter(self,s):
        
        ans=""
        ansdict=dict()
        flag=0
        for i in range(len(s)):
            if s[i] in ansdict:
                ansdict[s[i]]+=1
            else:
                ansdict[s[i]]=1
                
        for i in range(len(s)):
            if ansdict[s[i]]==1:
                ans=s[i]
                flag=1
                break
        if flag==0:
            return '$'   #if no repeating element
        else:
            return ans

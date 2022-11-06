def freq(l):
    if not l:
        return None
    else:
        ans=dict()
        for i in range(len(l)):
            if l[i] in ans.keys():
                ans[l[i]]+=1
            else:
                ans[l[i]]=1
        for x in ans:
            print(x," ",ans[x])

l=[10,10,10,20,20,30,30,40]
print(freq(l))

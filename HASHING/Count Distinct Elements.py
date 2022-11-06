# APPROACH 1
# def distinct(l):
#     if not l:
#         return None
#     else:
#         count =1
#         l.sort()
#         for i in range(1,len(l)):
#             if l[i]!=l[i-1]:
#                 count+=1
#         return count

# APPROACH 2
# def distinct(l):
#     if not l:
#         return None
#     else:
#         count =1
#         for i in range(1,len(l)):
#             if l[i] not in l[0:i]:
#                 count+=1
#         return count

#APPROACH 3
def distinct(l):
    s=set(l)
    return len(s)

l=[10,10,10,20,20,30,30,40]
print(distinct(l))

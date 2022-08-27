# a=[1,2,3,4,[5,6],7,8,[9,10,11],12]
# b=[]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):   
#                         b.append(a[i][j][k])
#                         sum+=a([i][j][k])
#                         k+=1
#             else:
#                 b.append(a[i][j])
#                 sum+=a[i][j]
#             j=j+1
#     else:
#         b.append(a[i])
#         sum+=a[i]
#     i=i+1
# print(b)        
# print(sum)



# a=[1,2,3,[2,3,4],[5,7,8],9,[10,11]]
# i=0
# b=[]
# s=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     b.append(a[i][j][k])
#                     s=s+(a[i][j][k])
#                     k=k+1
#             else:
#                 b.append(a[i][j])
#                 s=s+(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#         s=s+(a[i])
#     i=i+1
# print(s)
# print(a)                    



# a=[[1,2],[3,2],[3,4,5],[1,4]]
# sum=0
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a[i]):
#         s=s+(a[i][j])
#         j=j+1
#     sum=sum+s
#     i=i+1
# print(sum)      



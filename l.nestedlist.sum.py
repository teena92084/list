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
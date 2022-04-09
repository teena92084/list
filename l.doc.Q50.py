# def elementswise_joint(nums1,nums2):
#     result=[nums1+nums2 for nums1,nums2 in zip(nums1,nums2)]
#     return result
# nums1= [[10,20], [30,40], [50,60], [30,20,80]]   
# nums2 = [[61], [12,14,15], [12,13,19,20], [12]]
# print("Original lists:")
# print(nums1)
# print(nums2)
# print("\nJoin the said two lists element wise:")
# print(elementswise_joint(nums1, nums2))






# def elementswise_joint(m1,m2):
#     result=[m1+m2 for m1,m2 in zip(m1,m2)]
#     return result
# m1=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# m2=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]   
# print("orignal list")
# print(m1)
# print(m2)
# print("\n join the said list")
# print(elementswise_joint(m1,m2)) 



#Write a Python program to find the last occurrence of a specified item in a given list.
#Original list:


a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
#Last occurrence of f in the said list:
# 7
# #Last occurrence of c in the said list:
# 15
# ##Last occurrence of w in the said list:
# p=m.index("f")
# print(p)

# k=m.index("c")
# print(k)


# j=m.index("w")
# print(j
i=0
while i<len(a):
    if a[i]=="f":
        a1=i
    if a[i]=="c":
        a2=i
    if a[i]=="w":
        a3=i
    i=i+1
#print("f","c","w")
print(a1,a2,a3)
print("f=",a1)
print("c=",a2)
print("a3=",a3)

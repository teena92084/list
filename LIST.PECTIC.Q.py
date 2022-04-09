# marks=[
#     [78,76,94,86,88],
#     [91,71,98,65,76],
#     [95,45,78,52,49]
# ]
# sum=0
# i=0
# while i<len(marks[i]):
#     j=0
#     while j<len(marks[i]):
#         sum=sum+marks[i][j]
#         j=j+1
#     i=i+1
#     print(sum)        


# n=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# while i<len(n):
#     if n[i]>20 and n[i]<40:
#         count=count+1
#         print(count)
#     i=i+1    
# a=[23,14,56,12,19,12,76,99]
# i=0
# c=0
# c1=0
# p=[]
# b=[]
# s=0n=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# while i<len(n):
#     if n[i]>20 and n[i]<40:
#         count=count+1
#         print(count)
#     i=i+1    
# a=[23,14,56,12,19,12,76,99]
# i=0
# c=0
# c1=0
# p=[]
# b=[]
# s=0
# s2=0
# while i<len(a):
#     if a[i]%2==0:
#         p.append(a[i])
#         s=s+a[i]
#         c=c+1
#     else:
#         s2=s2+a[i]
#         b.append(a[i])
#         c1=c1+1
#     i=i+1
# print("count even=",c)
# print("count=",c1)
# print("sum odd",s2)
# print("sum even",s)
# print("a e",s/c)
# print("a o",s2/c1)

# # # l=[23,4,5,67,89]
# # # i=0
# # # max=0
# # # while i<len(l):
# # #     if l[i]>0:
# # #         max=l[i]
# # #     i=i+1
# # # print(max)           

# # # mark=[
# # #     [78,76,94,86,88],
# # #     [91,71,98,65,76],
# # #     [95,45,78,52,49]
# # # ]
# # # i=0
# # # s=0
# # # while i<len(mark):
# # #     j=0
# # #     while j<len(mark[i]):
# # #         s=s+mark[i][j]
# # #         j=j+1    
# # #     print(s//len(mark[i]))
# # #     i=i+1

# l=[5,6,7,87,7,79,5,43,3,3,3]
# i=0
# a=[]
# while i<len(l):
#     if l[i] not in a:
#         a.append(l[i])
#     i=i+1
# print(a)        

# kitna = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# c1=0
# c2=0
# c3=0
# while i<len(kitna):
#     if kitna[i]>100000 and kitna[i]<10000000:
#         c1=c1+1
#     elif kitna[i]<100000:
#         c2=c2+1   
#     else:
#         c3=c3+1
#     i=i+1 
# print("krod pati",c1) 
# print("lakpati",c2)           
# print("dawle",c3)   

# a=[]
# size=int(input("enter the size"))
# for i in range(size):
#     val=int(input("enter the value"))
#     a.append(val) 
# a.short( )
# print("maimum=",a[size-1])
# print("second=",a[size-2])
# print("thir=",a[size-3])    

# n=[1,2,2,5,8,4,8]
# i=0
# a=[]
# c=0
# while i<len(n):
#     if n[i] not in a:
#         a.append(n[i])
#         c=c+1
#     i=i+1
# print(c)
# print(a)        





# geekCodes = [1, 2, 3, 4]
# geekCodes.append([5,6,7,8])
# print(geekCodes)

# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list2[0] = 0
# print( list1)

# for i in range(4,31):
#     if i%2 == 0:
#         print(i, end=' ')

# a=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23
# ,24,25,26,27,28,29,30]
# for i in a:
#     if i%2==0:
#         print(i, end=' ')



# list1 = [4, 6, 8, 24, 12,2]
# max=sorted(list1)
# print(max[-1])


# ist = []
# list_1 =[]
# n = int(input("enter the total numbers inside list.: "))
# i = 1
# while(i <= n):
#     num = int(input("enter the numbers you want to insert into list: "))
# i +=1
# list.append(num)
# print(list,)
# list.sort()
# print(list)
# print(max(list))



# def cal(n):
#     sum=0
#     for i in range(1, 10, 1):
#         sum = sum +i
#     print(sum)
# rev = cal(11)


# aList = [4, 6, 8, 24, 12, 2]
# aList.sort(reverse=True)
# # print(aList.pop(0))
# # print(aList)


# num=[45,6,6,4,3,6.,99,9]
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)


# Index=int(input("num"))
# n=0
# for x in range (0,Index+1):
#     n+=x
# print(n)

# num=int(input("enter the water"))
# if num<10:
#     print("fill the water",10-num)
# elif num>=1 and num<=10:
#     print("no need water",)
# else:
#     print("over flow")        

# n=int(input("enter the number"))
# sum=0
# i=1
# while i<=n:
#     a=((n//100)%10)*100
#     b=((n//10)%10)*10
#     c=n%10
#     # i=i+1
#     print(a,"+",b,"+",c)
#     i=i+1
#     break


# name=(input("enter the name"))
# i=0
# l=len(name)
# while i<=0:
#     if l%2==0:
#         print("even")
#     else:
#         print("odd")  
#     i=i+1  
# 
# 
# j=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(j):
#         print(j[i]*i)
#         i=i+1 
          

# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(2*j,3*j,4*j,5*j,6*j,7*j,8*j,9*j,10*j)
#         j=j+1
#     i=i+1
#     break            


# a=[3,5,5,6,]
# i=0
# b=[]
# prod=1
# while i<len(a):
#     if a[i] not in b:
#         prod=prod*a[i]
         
#         b.append(a[i])
#     i=i+1
# print(b) 
# print(prod) 

# a=["tteena","tjj","pooja","krina"]
# print(a[2])

# # i=0
# while i<len(a):
#     print(i,a[i])
#     i=i+1

#Write a Python program to find the last occurrence of a specified item in a given list.
#Original list:
# m=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
#Last occurrence of f in the said list


#a=[1,2,[3,2,[5,6],3[4]]89,80]
#a=[1,2,3,4,[5,6],7,8,[9,10,11],12]
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


# m=[["t","e","e"],["n","a"],["k","n","w"]]
# b=[]
# i=0
# while i<len(m):
#     j=0
#     while j<len(m[i]):
#         b.append(m[i][j])
#         j=j+1
#     i=i+1
# b="".join(b)    
# print(b)        


# n=[6,1,3,5,6,3,1]
# b=[]
# i=0
# while i<len(n):
#     if n[i]not in b:
#         b.append(n[i])
#     i=i+1
# print(b)        


# m=[1,2,2,5,8,4,8]
# i=0
# a=[]
# c=0
# while i<len(m):
#     if m[i] not in a:
#         a.append(m[i])
#         c=c+1
#     i=i+1



# i=0
# a=[]
# c=0
# while i<len(m):
#     if m[i] not in a:
#         a.append(m[i])
#         c=c+1
#     i=i+1
# print(a)        
# print(c)



# a=[]
# size=int(input("entewr the size"))
# for i in range(size):
#     val=int(input("enter the value"))
#     a.append(val)
# a.sort()
# print("max n",a[size-1])
# print("second max",a[size-2]) 
# print ("third max",a[size-3])




# m=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# #List with maximum length of lists:
# (3, [13, 15, 17])
# #List with minimum length of lists:
# (1, [0])

# c=max(m)
# print(c)
# c=min(m)
# print(c)



# l=[9,1,1,9]
# i=0
# while i<len(l):
#     a=l[i]**2
#     i=i+1
#     print(a,end=" ")

# n=input("enter the number")
# i=0
# add=" "
# while i<len(n):
#     add=add+n[i]
#     j=0
#     while j<len(len(n)-(i+1)):
#         add+=" 0"
#         j=j+1
#     if i==(len(n)-1):
#         pass
#     else:
#         add+"+" 
#     i=i+1
# print(add)  



# a=[1000,2000,3000,4000]


# v=[454]
# l=len(v)
# i=l-1
# while i>=0:
#     print(v[i])
#     i=i-1

# n=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# while i<len(n):
#     c=max(n)
#     b=min(n)
#     i=i+1
# print(c)
# print(b)    


# l1=[10,20,30,40]
# l2=[100,200,300,400]
# i=0
# while i<len(l1):
#     j=3
#     while j<len(l2):
#         print(l1[i],l2[j])
#         j=i-1
#         i=i+1

# List = [[1,2],[3,2][5,6],[4],[89],[80]]
# sum=0
# i=0
# b=[]
# while i<len(List):
#     j=0
#     s=0
#     while j<len(List[i]):
#         s=s+List[i][j]
#         j=j+1
#     sum+=s
#     i=i+1
# print(sum)        

# a=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# i=0
# max=a[0]
# min=a[0]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     elif a[i]<min:
#         min=a[i]
#     i=i+1 
# print(int(max))
# print(int(min))          
# 
       
# l= [12, 4,6 ,8 ,34, 5 ,6 ,8]
# i=0
# max=0
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     i=i+1
# print(max)    
  
    
# l= [12, 4,6 ,8 ,34, 5 ,6 ,8]
# i=0
# min=0
# while i<len(l):
#     if l[i]<min:
#         min=l[i]
#     i=i+1
# print(min)        


# a=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
# i=0
# max=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])>max:
#             max=a[i][j]
# while i<len(a):
#     c=max(a)
#     i=i+1
# print(c)    

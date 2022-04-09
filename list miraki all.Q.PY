# print(a)
# print(type(a))

# print(a)
# a[0]="kirti"
# print(a)
# a[1]="kulsa"
# 
# frinds=["pooja","seena","AFASHANA","PRINKYA","anjali","suman","soniya"]
# frinds.append("alok")
# print(len(frinds))
# print(frinds)

# i=1
# while i<100:
#     n=i
#     s=0
#     order=len(str(n))
#     while n>0:
#         digit=n%10
#         s=s+digit**order
#         n//10
#     if s==n:
#         print(n,"is armstorng number") 
#     else:
#         pass
#     i=i+1   

# j=1
# while j<=100:
#     n=j
#     c=0
#     i=1
#     while i<=n:
#         if n%i==0:
#             c=c+1
#         i=i+1
#     if c==2:
#         print(j,"is prime number") 
#     else:
#         pass         
#     j=j+1   

# name_list=["pooja","kirti","swati","punam","teena"]
# print(name_list)
# name_list.pop()
# print(name_list)
# name_list.pop(2)
# print(name_list)


# student_list=["robin","pooja","karina","rina","teena"]
# index=0
# while index<len(student_list):
#     print(student_list[index])
#     index=index+1



# student_marks=[23,45,89,90,56,80]
# length=len(student_marks)
# index=0
# total_marks=0
# while index<len(student_marks):
#     total_marks=student_marks[index]+total_marks
#     index=index+1
# print("total_mark:"+str(total_marks)) 
# 
# 
   
# number=[50 ,40 ,70 ,60 ,12 ,45 ,56 ,89] 
# print(max(number))
# # print(max.) 


# place=["delhi","gujarat","rajasthan","panjab","kerela"]
# print(place[4])
# # print(place[3])
# # print(place[2])
# # print(place[1])
# # print(place[0])



# names_list=["n","i","t","i","n"]
# print("n"in names_list)
# print("naina" in names_list)
# print("anamana"in names_list)
# print("i"in names_list)
# print("teena"in names_list)

# magic_square = [
#  [8, 3, 4],
#  [1, 5, 9],
#  [6, 7, 2]
# ]

# print(type(magic_square))
# print (type(magic_square[0]))
# print (type(magic_square[1]))

# print(sum(magic_square[0]))
# print( sum(magic_square[1]))
# print (sum(magic_square[2]))

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]print(a)
# a[2]="manisa"
# print(a)
# a[3]="sannu"
# print(a)
# name_list=["rahul","shivani","kanya","anish"]
# print(name_list)
# print(type(name_list))



# bank_list=["brkgb","sbi","hsfc","BOB","RBI"]
# print(bank_list)
# print(type(bank_list))

# a=["teena","seena","swati
# print(list1[3])
# print(list1[4])


# marks=[
#     [78,76,94,86,88],
#     [91,71,98,65,76],
#     [95,45,78,52,49]
# ]
# sum=0
# i=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         sum=sum+marks[i][j]
#         j=j+1
#     i=i+1
# print(sum)        



# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# sum=0
# i=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         sum=sum+marks[i][j]
#         j=j+1
#     print(sum//len(marks[i]))    
#     i=i-1    

# This is not a magic square :

# magic_square=[
#     [8,3,4,0],
#     [1,5,9],
#     [6,7,2]
# ] 
# print(sum(magic_square[0]))
# print(sum(magic_square[1]))
# print(sum(magic_square[2]))     

# magic_square=[
#     [8,3,4,0],
#     [1,5,9],
#     [6,7,2]
# ]
# print(sum(magic_square[0]))
# print(sum(magic_square[1]))
# print(sum(magic_square[2]))

# 20 se 40 k beech number count krna

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# c=0
# while i<len(numbers):
#     if numbers[i]>20 and numbers[i]<40:
#         c=c+1
#     i=i+1
# print(c)

# a=[]
# size=int(input('enter the list size'))
# for i in range(size):
#     val=int(input("enter the value"))
#     a.append(val)
# a.sort() 
# print("max nmber",a[size-1])   
# print("second maxiumu number",a[size-2])
# print("third maximum number",a[size-3])






# l= [12, 4,6 ,8 ,34, 5 ,6 ,8]
# i=0
# max=0
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     i=i+1
# print(max)    


# e = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# while i<len(e):
#     if e[i]%2==0:
#         print(e[i],"even number")
#     else:
#         print(e[i],"odd number") 
#     i=i+1       











# student=["rishab","teena","tina","bhagwat","meena"]
# marks=[10,20,56,45,36,20]
# length=len(student)
# c=0
# while c<length:
#     print(student[c]+str(marks[c]))
#     c=c+1



 #Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers and the other is the average of odd numbers from the given list.   
# e= [23, 14, 56, 12,19,9,4,15, 25, 31, 42, 43]
# i=0
# s=0
# c=0
# s1=0
# c1=0
# while i<len(e):
#     a=e[i]
#     if a%2==0:
#         s=s+e[i]
#         c=c+1
#     else:      
#        s1=s1+e[i]
#        c1=c1+1
#     i=i+1
# print(s,c,"avrage=",s/c)
# print(s1,c1,"avrage=",s1/c1)
    
#     

#How many Crorepati?

# kitna= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# count=0
# counter=0
# countent=0
# while i<len(kitna):
#   if kitna[i]>100000 and kitna[i]<10000000:
#       count=count+1
#   elif kitna[i]<100000:
#       counter=counter+1
#   else:
#       countent=countent+1
#   i=i+1
# print("krodpati",counter)
# print("lakpati",count)
# print("diwale",countent)     



#Duplicates

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# a=[]
# while i<len(n):
#     j=n[i]
#     if j not in a:
#         a.append(j)
#     i=i+1
# print(a)                


#Count Occurences


  #: How to find all pairs in an array of integers whose sum is equal to the given number?



# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# a=[]
# while i<len(n):
#     j=0
#     while j<len(n):   
#       b=n[i]+n[j]
#       if number==b:
#         c=[n[i],n[j]]
#         a.append(c)
#       j=j+1
#     i=i+1
# print(a)
#    

# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# n=len(binary_number)
# i=0
# sum=0
# while i<n:
#   sum=sum+binary_number[n-1-i]*(2**i)
#   i=i+1
# print(sum)  


#Report Card - Part II
# list1 =[
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78]
# ]
# i=0
# while i<len(list1):
#   j=0
#   sum=0
#   while j<len(list1[i]):
#     sum=sum+list1[i][j]
#     j=j+1
#   print(sum//len(list1[i]))
#   i=i+1  

#Report Card - Part II

# marks =[## marks =[
#  marks =[
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78],
# [87, 67, 49, 68, 88]
# ]
# i=0
# while i<len(marks):
#   j=0
#   sum=0
#   while j<len(marks[i]):
#     sum=sum+marks[i][j]
#     j=j+1
#   print(sum//len(marks[i]))
#   i=i+1  

#Report Card
# marks =[
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78]
# ]
# i=0
# sum=0
# while i<len(marks):
#   j=0
#   while j<len(marks[i]):
#     sum=sum+marks[i][j]
#     j=j+1
#   i=i+1
# print(sum)    


# marks =[
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78],
# [87, 67, 49, 68, 88]
# ]
# i=0
# sum=0
# while i<len(marks):
#   j=0
#   while j<len(marks[i]):
#     sum=sum+marks[i][j]
#     j=j+1
#   i=i+1
# print(sum)


# i=10
# while i>=0:
#   print(10-i)
#   i=i-1






# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# s=0
# while i<=10:
#   s=s+a[i]
#   print(s)
#   i=i+1


# a=[["k","h"],["u","s","h"],["b","u"]]
# b=[]
# i=0
# while i<len(a):
#   j=0
#   while j<len(a[i]):
#     b.append(a[i][j])
#     j=j+1
#   i=i+1
# b="".join(b) 
# print(b)   

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# c=0
# c1=0
# s=0
# s1=0
# while i<len(elements):
#   if elements[i]%2==0:
#     s=s+elements[i]
#     c=c+1
#   else:
#     s1=s1+elements[i]
#     c1=c1+1
#   i=i+1
# print("countof even",c)
# print("count of odd number",c1) 
# print("sum of all sum number=",s+s1)
# print("sum of even number=",s)
# print("sum od odd number=",s1)
# print("average od even number=",s/c)
# print("average of odd numbrr=",s1/c1)   


# b={"computer","print","tv","teena"}
# print(type(b))
# print(b)


# diction_data={"teena:kanawar","age:20","higt:5.9ft","hoby:dance"}
# print(diction_data)
# print(type(diction_data))

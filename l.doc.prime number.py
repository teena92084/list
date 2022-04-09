
              

# list=[1,4,67,89,34,56,2,6,7]  
# prime=[]
# for i in list:
#     c=0
#     for j in range(1,i):
#         if i%j==0:
#             c=c+1
#     if c==1:
#         prime.append(i) 
# print(prime) 




# n=input("enter the number")
# a=int(n)
# l=len(n)
# i=0
# while i<len(n):
#     print(int(n[i])*(10**(l-1)),"+",end="")
#     i=i+1


# p=[454]
# l=len(p)
# i=l-1
# while i>=0:
#     print(p[i])
#     i-=1


i=1
l=[]
while i<=100:
    c=0
    j=1
    while j<=i:
        if i%j==0:
            c+=1
        j=j+1
    if c==2:
        l.append(i)
    i=i+1
print(l)                

i=1
while i<=100:
    c=0
    j=1
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        print(i,"prime")        
    i=i+1    
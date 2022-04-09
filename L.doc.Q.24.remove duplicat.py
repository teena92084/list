list = [1,2,3,1,2,2]       
        
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i+=1
print(b)
largest= None
num=[]
num_negative=int(input("how many negative number you want to enter?: "))
for i in range(num_negative):
    number=int(input("Enter the number:"))  
    num.append(number)
for j in num : 
    if j >=0 :
        continue
    elif largest==None:
        largest=j
    elif j > largest:
        largest=j
print(largest)
       
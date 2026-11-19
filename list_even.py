numbers=[10,20,15,30,25,40,35]
even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)

    else:
        odd.append(i)    
print(even) 
print(odd)       
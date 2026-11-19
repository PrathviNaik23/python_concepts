numbers=[10,20,10,30,20,40,50,30]
n=[]

for i in numbers:
    if numbers.count(i)>1:
        if i not in n:
            n.append(i)
print(n)        
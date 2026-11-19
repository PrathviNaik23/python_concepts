numbers=[15,8,22,15,10,30,8,25,40,22]
greater=[]
lesser=[]
duplicate=[]
for i in numbers:
    if i>20:
        greater.append(i)
    if i<20:
        lesser.append(i)
    if numbers.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
print(greater)
print(lesser)
print(duplicate)                  
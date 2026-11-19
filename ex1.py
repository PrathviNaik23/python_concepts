numbers=[12,5,8,21,5,30,12,18,7,21]
even=[]
odd=[]
duplicate=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    if numbers.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
print(even)
print(odd) 
print(duplicate)           
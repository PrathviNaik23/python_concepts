list=[10,20,30,40,50]
sum=0
largest=list[0]
smallest=list[0]
for i in range(len(list)):
    sum+=list[i]
    
    if list[i]>largest:
        largest=list[i]

    if list[i]<smallest:
        smallest=list[i]

average=sum/len(list)

print(sum)
print(largest)
print(smallest)
print(average)
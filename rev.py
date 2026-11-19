r=int(input("enter number :"))
reverse = 0

while r>0:
    n=r%10
    r//=10
    reverse=reverse*10+n
print(reverse)    
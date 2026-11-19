n=int(input("enter number :"))
original=n
reverse=0
while n>0:
    digit=n%10
    n//=10
    reverse=reverse*10+digit
print(reverse)    
if original == reverse:
    print(f"{original} is palindrom") 
else:
    print(f"{original} is not palindrom")    
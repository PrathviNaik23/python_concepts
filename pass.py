a=int(input("enter english marks"))
b=int(input("enter maths marks"))
c=int(input("enter python marks"))
d=int(input("enter dbms marks"))
e=int(input("enter java marks"))
print()
Total = a+b+c+d+e
Average = Total/5
Percentage = (Total/500)*100

if a>=40 and b>=40 and c>=40 and d>=40 and e>=40:
    result="Pass"
else:
    result="Fail"


if result == "Fail":
    Grade="Fail"
elif Percentage >= 90:
    Grade="A"
elif Percentage >= 75:
    Grade="B"
elif Percentage >= 60:
    Grade="C"
elif Percentage >= 40:
    Grade="D" 

print(f"\nTotal :{Total}")   
print(f"Average :{Average}")
print(f"Percentage :{Percentage}%") 
print(f"Grade :{Grade}")  
print(f"Result :{result}")             
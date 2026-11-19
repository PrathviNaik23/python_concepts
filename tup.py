
while True:
    a=input('1.Addition\t2.Substraction\t3.Multiplication\t4.Division\nenter your operation : ').strip()

    n=int(input('enter first number :'))
    m=int(input('enter second number :'))

    if a=='1':
        print(n+m)
    elif a=='2':
        print(n-m)
    elif a=='3':
        print(n * m)
    elif a=='4':
        print(n/m)            
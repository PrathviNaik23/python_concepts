val1=int(input('val1: '))
val2=int(input('val2: '))
val3=int(input('val3: '))

if val1>val2 and val1>val3:
    print(f'{val1} is greater')
elif val2>val1 and val2>val3:
    print(f'{val2} is greater')
else:
    print(f'{val3} is greater')        
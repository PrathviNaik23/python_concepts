n=input('enter: ')
a=ord(n)
if a>=65 and a<=90:
    print('upper case')
elif a>=97 and a<=122:
    print('lower case')
elif a>=48 and a<=57:
    print('numbers')
else:
    print('spcl_char')            
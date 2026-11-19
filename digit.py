n=int(input('n= '))
if -9<=n<=9:
    print('single digit')
elif (-99 <= n <=-10) or (10 <=n <=99):
    print('double digit')  
elif -999<=n<=-100 or 100<=n<=999:
    print('three digit')     
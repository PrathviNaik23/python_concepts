password='12345'
limit=3
while True:
    n=input('enter password: ')
    if n==password:
        print('password is correct')
        exit()
    else:
        limit-=1
        if limit <= 3:
            print('worng paSSWORD')
            print(f'{limit} attempt left')
            if limit == 0:
                print ('limit reached')
                exit()
                
                

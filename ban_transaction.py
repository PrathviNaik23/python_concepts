balance=0
transaction=[]
while True:
    n=input('deposite\twithdraw\tcheck_balance\ttransactions\tcancel\nchoose option: ')
    if n=='deposite':
        amt=int(input('enter the amount: '))
        balance+=amt
        transaction.append(f'deposited: {amt}')
        print(f'{amt} deposited succeesfully')
    elif n=='withdraw':
        if balance>0:
            amt=int(input('enter amount: '))
            if amt<=balance:
                balance-=amt
                transaction.append(f'withdrawn: {amt}')
                print(f'{amt} withdrawn succesfully')   
            else:
                print('insufficient balance') 
    elif n=='check_balance':
        print(balance)     
    elif n=='transactions':
        for i in transaction:
            print(i)
    elif n=='cancel':
        print('THANKS FOR USING BANK')  
        exit()      
    else:
        print('invalid choice') 

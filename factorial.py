balance=0
while True:
    n=(input('Deposite\tWithdraw\tbalance\tcancel\noption:'))
    match n:
      case'deposite':
         amt=int(input('enter the amount: '))
         balance+=amt
         print(f'{amt} deposited\navailable balance {balance}')
      case 'withdraw':
         amt=int(input('enter the amount: '))
         if amt<balance:
            print('insuffitient balance')
         else:
            balance-=amt
            print(f'{amt} withdrawn successful\navailable balance {balance}')
      case 'balance':
         print(f'available balance: {balance}')               
      case 'cancel':
         exit() 
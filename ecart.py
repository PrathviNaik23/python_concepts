cart=[]
cart_price=[]
while True:
    choice=input('1.add_cart\t2.view_cart\t3.total_cart\nOption(1,2,3): ')
    if choice=="1":
        item=input('add a item: ')
        cart.append(item)
        print(f'{item} added to cart')
        price=int(input('enter the item price: '))
        cart_price.append(price)

    elif choice=='2':
        if  not cart:
            print('please add a items to cart')    
        else:
            for i in range(len(cart)):
                print(f'{cart[i]}, {cart_price[i]}') 
               

    elif choice=='3':
        total_price=0
        for i in range(len(cart_price)):
            total_price+=cart_price[i]
            print(f'number of items: {len(cart)}')
        print(f'total price: {total_price}')
        break
    else:
        print('invalid choice')    
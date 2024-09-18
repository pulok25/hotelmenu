#define the menu of the resturant 
menu = {
    'cold coffee':40,
    'black coffee': 30,
    'chocolate coffee':40,
    'dudh cha':15,
    'malai cha':40,
    'rong cha': 10,
    'malta cha': 20,
    'cookies': 5,
}

#Greetings
print("Welcome to SANZ CAFE")
print('cold coffee: 40tk\nblack coffee : 30tk \nchocolate coffee: 40tk\ndudh cha: 15tk\nmalai cha: 40tk\nrong cha:10tk\nmalta cha:20tk\ncookies:5tk   ')

order_total = 0
item1 = input('Enter the name of item:')

if item1 in menu:
    order_total +=menu[item1]
    print(f'Your item {item1} has been added to your order')
else:
    print(f'this item {item1} is not available in our Cafe Sir')

another_order = input('Do you want need anything else Sir ? (Yes/No)')
if another_order == 'Yes':
    item2 = input('Enter the name of second item :')
    if item2 in menu:
        order_total += menu[item2]
        print(f'Your item {item2} has been added to order')
    else:
        print(f'this item {item2} is not available in our Cafe sir')

print(f'Your bill is {order_total} tk Sir')
    

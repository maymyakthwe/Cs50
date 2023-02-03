menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


order_list = []
while True:
    order = input('What do you wanna order?')
    order = order.title()
    if order in "control-d":
        break
    order_list.append(order)
    total_price = 0
    for each in order_list:
        if each in menu.keys():
            total_price = total_price+menu[each]
            print(total_price)
        else:
            continue

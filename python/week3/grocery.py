order_list = []
to_check = []
x = 1

while True:
    order = input('What do you wanna order?').upper()

    if order in "CONTROL-D":
        order_list = sorted(order_list, key=lambda d: d['name'])
        for each in order_list:
            print(each['number'], ' ', each['name'])
        break
    elif order in to_check:
        x = x+1
        order_list = list(
            filter(lambda d: not d['name'] in order, order_list))
        to_add = {'name': order, 'number': x}
        order_list.append(to_add)
    else:
        to_add = {'name': order, 'number': 1}
        order_list.append(to_add)
        to_check.append(order)

# order_list = []


# while True:
#     order = input('What do you wanna order?')
#     to_add = {'name': order, 'number': 1}
#     if order in "exit":
#         break
#     else:
#         order_list.append(to_add)

# print(order_list)

# to_check = []
# for each in order_list:
#     to_check.append(each['name'])
# print(to_check)


exampleSet = [{'type': 'type1'}, {'type': 'type2'},
              {'type': 'type2'}, {'type': 'type3'}]
keyValList = ['type2', 'type3']
expectedResult = list(
    filter(lambda d: not d['type'] in keyValList, exampleSet))
print(expectedResult)

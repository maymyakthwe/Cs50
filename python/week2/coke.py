amount_due = 50
while amount_due > 0:
    print("Amount Due: "+str(amount_due))
    coin = int(input("Insert Coin:"))
    if coin in [5, 10, 25]:
        amount_due -= coin
print("Changed Owe:"+str(abs(amount_due)))

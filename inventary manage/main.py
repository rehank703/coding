import funct

wuw = input("what you want to do\n1. Add\n :")

if wuw == "1":
    product = input("enter product name: ")
    price = input("Price of product: ")
    quantity = input("quantity of product: ")
    funct.addpro(product, price, quantity)

wuw2 = input("do you want to\n2. update\n3. delete\n: ")

if wuw2 == "2":
    chan = input("what do you want to edit\n1. product\n2. price\n3. quantity")
    if chan == "1":
        product = input("enter product name: ")
    elif chan == "2":
         price = input("Price of product: ")
    elif chan == "3":
         quantity = input("quantity of product: ")
    else:
        print("error")
    funct.addpro(product, price, quantity)
elif wuw2 == "3":
    del product, price, quantity
    print("deleted successfully")
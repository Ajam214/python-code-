items = [int,float, "Ali", 212, 252, 256, 363, 555,525,6]


for item in items:
    if str(item).isnumeric() and item>6:
        print(item)
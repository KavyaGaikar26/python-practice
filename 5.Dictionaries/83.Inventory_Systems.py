inventory = {
    "apple": 10,
    "banana": 20,
    "milk": 5
}

operation = input("Enter the Operation:")

if operation == "add item":
    item = input("Enter your item: ")
    quantity = int(input("Enter your quantity: "))
    inventory[item] = quantity

elif operation == "remove item":
    item = input("Enter your item: ")
    if item in inventory:
        del inventory[item]
    else:
        print("Item not found")

elif operation == "update quantity":
    item = input("Enter your item: ")
    quantity = int(input("Enter your quantity: "))
    inventory[item] = quantity   

elif operation == "search item":
    item = input("Enter your item: ")
    if item in inventory:
        print("Quantity:", inventory[item])
    else:
        print("Item not found")


print(inventory)

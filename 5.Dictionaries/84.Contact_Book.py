contacts = {
    "Rahul": "9876543210",
    "Priya": "9123456780",
    "Amit": "9988776655"
}

operation = input("Enter the Operation:")

if operation == "add contact":
    name = input("Enter the Name:")
    phone_number = input("Enter the phone number:")
    contacts[name] = phone_number

elif operation == "remove contact":
    name = input("Enter the Name:")
    if name in contacts:
        del contacts[name]
    else:
        print("Name not Found")

elif operation == "search contact":
    name = input("Enter the Name:")
    if name in contacts:
        print("Phone Number:", contacts[name])
    else:
        print("Name not Found")

elif operation == "update contact":
    name = input("Enter the Name:")
    if name in contacts:
        phone_number = input("Enter the phone number:")
        contacts[name] = phone_number
    else:
        print("Name not Found")


print(contacts)
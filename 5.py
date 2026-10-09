menu = {
    "Momo": 150,
    "Chowmein": 120,
    "Pizza": 350,
    "Burger": 200,
    "Pasta": 250,
    "Fried Rice": 180,
    "Sandwich": 150,
    "French Fries": 100
}

order = []

def displaymenu():
    print("\n----- MENU -----")
    for item in menu:
        print(item, "- Rs.", menu[item])

def addorder(name, quantity):
    if name not in menu:
        raise ValueError("Food item not found!")

    order.append({"name": name, "quantity": quantity})

def calculatebill():
    subtotal = 0
    for item in order:
        subtotal += menu[item["name"]] * item["quantity"]

    tax = subtotal * 0.13
    total = subtotal + tax
    return subtotal, tax, total

def displayorder():
    print("\n----- YOUR ORDER -----")
    for item in order:
        price = menu[item["name"]] * item["quantity"]
        print(item["name"], "x", item["quantity"], "= Rs.", price)

while True:
    displaymenu()
    name = input("\nEnter food item (or 'done' to finish): ").title()

    if name == "Done":
        break

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero!")

        addorder(name, quantity)
        print("Item added successfully!")

    except ValueError as e:
        print(e)

displayorder()

subtotal, tax, total = calculatebill()

print("\n----- FINAL BILL -----")
print("Subtotal: Rs.", subtotal)
print("Tax (13%): Rs.", round(tax, 2))
print("Final Total: Rs.", round(total, 2))
print("Thank you for ordering!")
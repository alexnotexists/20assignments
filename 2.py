products = {
    "Laptop": {"price": 80000, "quantity": 5},
    "Mobile": {"price": 30000, "quantity": 10},
    "Keyboard": {"price": 1500, "quantity": 8},
    "Mouse": {"price": 800, "quantity": 12},
    "Headphones": {"price": 2000, "quantity": 6},
    "Monitor": {"price": 15000, "quantity": 4}
}

cart = {}

def addtocart(name, quantity):
    if name not in products:
        raise ValueError("Product does not exist!")

    if quantity > products[name]["quantity"]:
        raise ValueError("Not enough quantity available!")

    products[name]["quantity"] -= quantity

    if name in cart:
        cart[name] += quantity
    else:
        cart[name] = quantity

    print("Product added to cart!")

def totalprice():
    total = 0
    for name in cart:
        total += products[name]["price"] * cart[name]
    return total

def displaycart():
    for name in cart:
        price = products[name]["price"]
        quantity = cart[name]
        print(name, "x", quantity, "=", price * quantity)

def displayproducts():
    print("Available Products:")
    for name in products:
        print(name, "- Price:", products[name]["price"],
              "- Available Quantity:", products[name]["quantity"])

while True:
    displayproducts()

    name = input("Enter product name (or 'done' to finish): ").title()

    if name == "Done":
        break

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero!")

        addtocart(name, quantity)
        displayproducts()

    except ValueError as e:
        print(e)

print("FINAL BILL")
displaycart()
print("Total Price =", totalprice())
print("Thank you for shopping!")
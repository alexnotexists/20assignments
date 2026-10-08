cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]
new_cart = []
for item in cart:
    if item not in new_cart:
        new_cart.append(item)
new_cart.append("cheese")
new_cart.remove("bread")
new_cart.sort()
print("Final cart:", new_cart)
print("Number of items:", len(new_cart))
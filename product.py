product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}
print("Name : ",product["name"])
print("Brand : ",product["brand"])
print("Price",product["price"])
print("Quantity",product["quantity"])
print("Total Value : ",product["price"]*product["quantity"])
product["quantity"]=2
print("After Selling 3 Laptops, Quantity",product["quantity"])


employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}
del(employee["age"])
del(employee["city"])
print(employee)
employee.pop("email",None)
print(employee)
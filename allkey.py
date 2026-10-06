book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2025,
    "price": 500
}
print(book.keys())
print(book.values())
print(book.items())
for key in book:
    print(key,"=",book[key])
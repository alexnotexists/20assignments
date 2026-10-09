books = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "available": True},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "available": True},
    {"title": "The Alchemist", "author": "Paulo Coelho", "available": True},
    {"title": "Atomic Habits", "author": "James Clear", "available": True}
]

def searchbook(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise ValueError("Book not found!")

def borrowbook(title):
    book = searchbook(title)
    if book["available"]:
        book["available"] = False
        print("Book borrowed successfully!")
    else:
        print("Book is already borrowed!")

def returnbook(title):
    book = searchbook(title)
    if book["available"] == False:
        book["available"] = True
        print("Book returned successfully!")
    else:
        print("Book is already available!")

def displaybooks():
    print("Library Books:")
    for book in books:
        print("Title:", book["title"],
              "| Author:", book["author"],
              "| Available:", book["available"])

while True:
    print("1. Search Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            title = input("Enter book title: ")
            book = searchbook(title)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Available:", book["available"])

        elif choice == "2":
            title = input("Enter book title to borrow: ")
            borrowbook(title)

        elif choice == "3":
            title = input("Enter book title to return: ")
            returnbook(title)

        elif choice == "4":
            displaybooks()

        elif choice == "5":
            print("Thank you for using the library!")
            break

        else:
            print("Invalid choice!")

    except ValueError as e:
        print(e)
student = {
    "name": "Hari",
    "age": 19,
    "course": "Python",
    "city": "Lalitpur"
}
userkey=input("Enter a key : ")
if userkey in student:
    print(f"{userkey} exists")
else:
    print(f"{userkey} doesnot exist")

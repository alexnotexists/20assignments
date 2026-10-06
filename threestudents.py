students = {
    101: {
        "name": "Ram",
        "age": 20,
        "course": "Python"
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "Java"
    },
    103: {
        "name": "Hari",
        "age": 19,
        "course": "Python"
    }
}

print(students)
print("\n")

print(students[101])
print("\n")

students[103]["course"] = "Java"
print(students[103])
print("\n")

students[104] = {
    "name": "Ram",
    "age": 67,
    "course": "DataScience"
}

print(students)
print("\n")

students.pop(101)
print(students)
print("\n")

id = int(input("Enter ID : "))

if id in students:
    print(students[id])
else:
    print("Student ID not found")
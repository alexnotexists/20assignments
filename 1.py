def totalmarks(name):
    for student in students:
        if student["name"] == name:
            total = student["Math"] + student["English"] + student["Science"]
            return total
    raise ValueError("Student Not Found!")

def percentagemarks(name):
    for student in students:
        if student["name"] == name:
            total = student["Math"] + student["English"] + student["Science"]
            percentage = (total / 3) 
            return percentage
    raise ValueError("Student Not Found!")

students = [
    {"name": "Ram", "Math": 80, "English": 75, "Science": 85},
    {"name": "Sita", "Math": 90, "English": 88, "Science": 92},
    {"name": "Hari", "Math": 70, "English": 78, "Science": 72},
    {"name": "Gita", "Math": 85, "English": 80, "Science": 89},
    {"name": "Shyam", "Math": 65, "English": 70, "Science": 75}
]

try:
    name = input("Whose Marks Do You Want To Calculate: ").capitalize()
    tot = totalmarks(name)
    per = percentagemarks(name)
    print(f"Total = {tot}")
    print(f"Percentage = {per:.2f}%")

except ValueError as e:
    print(e)

except KeyError:
    print("Subject mark is missing!")
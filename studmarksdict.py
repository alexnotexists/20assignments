marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}
print(marks.keys())
print(marks.values())
print(sum(marks.values()))
print(sum(marks.values())/len(marks))
print(max(marks.values()))
print(min(marks.values()))
print(list(marks.keys())[list(marks.values()).index(max(marks.values()))])
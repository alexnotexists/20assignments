marks = [45, 78, 62, 89, 55, 92, 38, 76]
highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / len(marks)
count = 0
for mark in marks:
    if mark > average:
        count = count + 1
marks.sort()
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above average:", count)
print("Ascending order:", marks)
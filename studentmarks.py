marks = [75, 82, 68, 90, 55, 88, 72, 95]
print(marks)
print("TOTAL : ",sum(marks))
print("AVG : ", sum(marks)/len(marks))
print("HIGHEST : ",max(marks))
print("LOWEST : ",min(marks))
count=0
for items in marks:
    if items>=75:
        count+=1
print(count)
marks.sort(reverse=True)
print(marks)
anothermarks=int(input("Enter another marks : "))
marks.append(anothermarks)
print(marks)
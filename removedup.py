numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30]
unique=[]
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]!=numbers[j]:
            unique.append(numbers[j])
print(unique)
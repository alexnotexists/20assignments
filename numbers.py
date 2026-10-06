numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first_five=[numbers[i] for i in range(0,5)]
last_five=[numbers[i] for i in range(-5,0)]
print(first_five)
print(last_five)
index2_6=[numbers[i] for i in range (2,7)]
print(index2_6)
everysecond=[numbers[i] for i in range(1,11,2)]
print(everysecond)
numbers.reverse()
print(numbers)
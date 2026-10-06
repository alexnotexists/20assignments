fruits = [
    "apple", "banana", "apple",
    "orange", "banana", "apple",
    "mango", "orange", "banana"
]
count={
}
ac=0
bc=0
oc=0
mc=0
for i in range(0,len(fruits)):
    if(fruits[i]=="apple"):
        ac+=1
    elif(fruits[i]=="banana"):
        bc+=1
    elif(fruits[i]=="orange"):
        oc+=1
    else:
        mc+=1
count["apple"]=ac
count["banana"]=bc
count["orange"]=oc
count["mango"]=mc
print(count)

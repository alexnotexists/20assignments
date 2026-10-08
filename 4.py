sentence = input("Enter a sentence: ")
sentence = " ".join(sentence.split())
sentence = sentence.lower()
words = sentence.split()
print("Total words:", len(words))
count = 0
for word in words:
    if word == "python":
        count = count + 1
print("Python appears:", count, "times")
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
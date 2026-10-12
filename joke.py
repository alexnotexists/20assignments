
import pyjokes

for i in range(3):
    joke = pyjokes.get_joke()
    print(joke)
    print()

while True:
    answer = input("Do you want another joke? (yes/no): ").lower()

    if answer == "yes":
        print(pyjokes.get_joke())
    else:
        print("Thank you!")
        break

from colorama import Fore, init

init(autoreset=True)

name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

print(Fore.CYAN + "Student Name: " + name)

if marks >= 40:
    print(Fore.GREEN + "PASS")
else:
    print(Fore.RED + "FAIL")

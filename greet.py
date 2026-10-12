import emoji

name = input("Enter your name: ")

print("Hello", name, emoji.emojize(":grinning_face:"))

activity = input("What is your favorite activity? ")

print("You enjoy", activity, emoji.emojize(":thumbs_up:"))
print("Keep learning Python!", emoji.emojize(":red_heart:"))

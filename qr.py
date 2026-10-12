import qrcode

name = input("Enter your name or a short message: ")

img = qrcode.make(name)
img.save("my_qrcode.png")

print("QR code saved as my_qrcode.png")

website = input("Enter your favorite website URL: ")

img = qrcode.make(website)
img.save("favorite_website.png")

print("Website QR code saved as favorite_website.png")

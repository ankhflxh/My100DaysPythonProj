import string
import random

print("WELCOME TO MY PASSWORD GENERATOR")
alphabet = string.ascii_letters
symbol = string.punctuation
number = ['0', '1', '2', '3', '4', '5', '6','7', '8', '9']
letter = int(input("How many letters would you like in your password?:\n"))
sym = int(input("How many symbols would you like in your password?:\n"))
num = int(input("How many numbers would you like in your password?:\n"))

password = []
for char in range(0, letter):
    password += random.choice(alphabet)
for char in range(0, sym):
    password += random.choice(symbol)
for char in range(0, num):
    password += random.choice(number)


random.shuffle(password)
new_password = ""
for char in password:
    new_password += char
print(f"Your password is: {new_password}")


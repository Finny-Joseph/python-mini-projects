import random
import string

print("===== Password Generator =====")

# Users choices
length = int(input("Enter password length: "))
use_numbers = input("Include Numbers? (y/n): ")
use_symbols = input("Include Symbols? (y/n): ")

#Figure out what needs to be used
characters = string.ascii_letters

if use_numbers.lower() == "y":
    characters += string.digits

if use_symbols.lower() == "y":
    characters += string.punctuation

print("Character Pool: ",characters)

#Generate the Password
password = ""

for i in range(length):
    password += random.choice(characters)

#Print the password
print("Generated password:",password)
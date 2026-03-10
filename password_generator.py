import random
import string

print("===== Password Generator =====")

# Users choices
length = int(input("Enter password length: "))
use_numbers = input("Include Numbers? (y/n): ")
use_symbols = input("Include Symbols? (y/n): ")

#Figure out what needs to be used
characters = list(string.ascii_letters)

if use_numbers.lower() == "y":
    characters.extend(list(string.digits))

if use_symbols.lower() == "y":
    characters.extend(list(string.punctuation))

#Generate the Password
password_list = []

for i in range(length):
    password_list.append(random.choice(characters))

password = "".join(password_list)

#Print the password
print("Generated password:",password)
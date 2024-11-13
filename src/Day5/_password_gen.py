import string
import random
letters_upper = list(string.ascii_uppercase)
letters_lower = list(string.ascii_lowercase)
letters = letters_lower + letters_upper
numbers = list(string.digits)
symbols = list(string.punctuation)

password_list = []
user_password = ""


n_letters =  int (input("How many letters would you like to generate?\n "))
n_symbols =  int (input("How many symbols would you like to generate?\n "))
n_numbers =  int (input("How many number would you like to generate?\n "))

for letter in range(1, n_letters + 1):
    rand_letters = random.choice(letters)
    password_list.append(rand_letters)

for number in range(1, n_numbers + 1):
    rand_numbers = random.choice(numbers)
    password_list.append(rand_numbers)
for symbol in range(1, n_symbols + 1):
    rand_symbols = random.choice(symbols)
    password_list.append(rand_symbols)

print(password_list)
random.shuffle(password_list)
for char in password_list:
    user_password += char

print(user_password)














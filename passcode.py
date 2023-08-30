import random

def isValid(value):
    while (value <= 0 or type(value) != int):
       value = int(input("Invalid entry. Try again:"))
    return value


print("\n---WELCOME TO THE RANDOM PASSWORD GENERATOR---")

availableCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!%$_'

number = int(input("Please enter how many passwords you would like to generate: "))
isValid(number)

length = int(input('Password(s) length: '))
isValid(length)

print('\nDrumroll please... Here are your passwords:\n')

for password in range(number):
    passwords = ''
    for i in range(length):
        passwords += random.choice(availableCharacters)
    print(passwords)

print('\nThose passwords look pretty random to me. Goodbye!\n')
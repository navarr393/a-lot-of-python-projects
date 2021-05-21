import random
from random import randint

# do not modify chars
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

number = input('Number of passwords: ')
number = int(number)

length = input('length of password: ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password+=random.choice(chars[:62])

    print(password)

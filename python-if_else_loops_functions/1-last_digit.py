#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number

if number < 0:
    number = -(number)

last_digit = number % 10
if num < 0:
    number = num
    last_digit = -(last_digit)

if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
elif last_digit < 6:
    message = "and is less than 6 and not 0"

print("Last digit of", number, "is", last_digit, message)

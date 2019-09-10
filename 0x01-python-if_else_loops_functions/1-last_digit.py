#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# sign standard format, boolean expression
sign = True if number >= 0 else False
# positve %10 and negative conditions
last_digit = number % 10 if sign else (-number) % 10
last_digit = -last_digit if not sign else last_digit
print("Last digit of {:d} is {}".format(number, last_digit), end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

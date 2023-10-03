#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
positive_last_digit = number % 10
negative_last_digit = number % -10

if number >= 0:
    if positive_last_digit > 5:
        print(f"Last digit of {number} is\
 {positive_last_digit} and is greater than 5")
    elif positive_last_digit < 6 and positive_last_digit != 0:
        print(f"Last digit of {number} is\
 {positive_last_digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {positive_last_digit} and is 0")

elif number <= 0:
    if negative_last_digit < 6 and negative_last_digit != 0:
        print(f"Last digit of {number} is\
 {negative_last_digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {negative_last_digit} and is 0")

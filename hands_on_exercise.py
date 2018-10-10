"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random
import math
import random

# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi), pi)
print("#"*100)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print("Value of i is", i)
if i < 50:
    print("i is less than 50")
else:
    print("i is greater than 50")
print("#"*100)
# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print('Randomly picked fruit is ', picked_fruit)
if picked_fruit == 'orange':
    print('Color of the picked fruit is Orange')
elif picked_fruit == 'strawberry':
    print('Color of the picked fruit is Red')
else:
    print('Color of the picked fruit is Yellow')
print("#"*100)
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(num1, num2):
    output = num1 * num2
    return output

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiply(12, 96))

print("48 x 17 =",multiply(48, 17))

print("196523 x 87323 =",multiply(196523, 87323))
print("#"*100)
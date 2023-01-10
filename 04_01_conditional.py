print('Task 1 - calculate sum')
# Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.
# If the values are equal then calculate triple value of their sum.
# Print out an appropriate message to the user.

a = int(input('First number '))
b = int(input('Second number '))
c = int(input('Third number '))
if a == b == c:
    print('The tripple sum is: ', (a + b + c) * 3)
else:
    print('The sum is: ', a + b + c)


print('Task 2 - get the difference')
# Your task is to write a Python program to get the difference between a two given numbers (prompted by user).
# If the first number is greater than second then calculate double difference between numbers.
# Otherwise calculate the absolute difference between numbers.
# Print out an appropriate message to the user.

a = int(input('First number: '))
b = int(input('Second number: '))
if a > b:
    print('The result of calculation is ', abs((a - b) * 2))
elif a - b == 0:
    print('The result of calculation is 0')


print('Task 3 - odd or even number')
# Your task is to write a Python program to find whether a given number (prompted from the user) is even or odd. Print out an appropriate message to the user.

a = int(input('Number to check: '))
if a / 2 == 0:
    print(a, ' is an even number!')
else:
    print(a, ' is an odd number!')


print('Task 4 - circle area')
# Your task is to write a Python program which accepts (prompts) the float radius of a circle from the user and compute its area.
# Round the result to two decimals!
# Print out an appropriate message to the user.

from math import pi
r = float(input('Input the radius of the circle: '))
print('The area of the circle with radius ', str(r), 'is ', round(pi * (r ** 2), 2))



print('Task 5 - guess a number')
# Your task is to write a Python program to guess a number between 1 to 9.
#
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
#
# Hint: you don't know the random module yet, so set your number to guess hard-coded in your program.


a = int(input('Guess a number between 1 and 10 until you get it right: '))
while a != 7 or a > 10:
    a = int(input('Guess a number between 1 and 10 until you get it right: '))
print('Well guessed!')



print('Task 6 - Celsius to Fahrenheit conversion')
# Your task is to write a Python program to convert temperatures to and from Celsius, Cahrenheit.
#
# In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
# In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.
#
# Note : User should be prompted twice:
#
# to enter a temperature,
# to enter a shortcut for given scale (C for Celsius, F for Fahrenheit).


print("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius): ")
celc = int(input("Input the value of temperature you'd like to convert from C To F: "))
f = (celc * 1.8) + 32
print('The temperature in Fahrenheit is ', f)

fahr = int(input("Input the value of temperature you'd like to convert from F To C: "))
c = (fahr - 32) / 1.8
print('The temperature in Celcius is ', c)





print('Task 7 - pattern')
# Your task is to write a Python program to construct the following pattern. Upper part should be done in one line of code without using a loop.
# Lower part can be done with any kind of loop or also with one line of code and without loops.

print("\n *\n **\n ***\n ****\n *****\n ******\n *******\n ******\n *****\n ****\n ***\n **\n *")


print('Task 8 - Fibonacci series')
# Your task is to write a Python program to get the Fibonacci series between 0 to 50.
#
# Note: The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
#
#

# f_num = int(input('Enter number'))
# x = 0
# y = 1
# while f_num < 1 or f_num > 50:
#     f_num = int(input('Enter number'))
# while y <= f_num:
#     print(y)
#     x, y = y, x + y


a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
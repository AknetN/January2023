# Task 1 - fix the FizzBuzz
# Your Task is to fix program non - working correctly.The FizzBuzz problem:
# FFor all integers between 1 and 99 (include both):
## print 'fizz' for multiples of 3,
# print 'buzz' for multiples of 5,
# print 'fizzbuzz' for multiples of 3 and 5.


three_mul = 'fizz'
five_mul = 'buzz'
eight_mul = 'fizzbuzz'
num1 = 3
num2 = 4
num3 = 5
for i in range(1, 100):
    # % or modulo division gives you the remainder

    if i % num1 == 0:
        print(i, three_mul)
    elif i % num2 == 0:
        print(i, five_mul)
    elif i % num1 == 0 or i % num3 == 0:
        print(i, eight_mul)






# Task 2 - summing integers
# Your task is to fix program non-working correctly. The problem:
#
# sum integers from 1 to 5 using while loop
# calculate what result should be and what you get after running the program
# Program with bug:


n = 5
number = 1
sum = 0
while number <= n:
    sum = sum + number
    number = number + 1
print("Sum = ", sum)






# Task 3 - summing integers with range()
# Your task is to fix program non-working correctly. The problem:
#
# sum integers from 1 to 5 using range() function
# calculate what result should be and what you get after running the program
# Program with bug:

n = 5
sum = 1
for num in range(n):
    sum = sum + num
    num = num + sum
print("Sum = ", num)





# Task 4 - printing in loops
# Your task is to fix program non-working correctly. The problem:
#
# there are 4 short programs with loops, that should print some numbers, but they don't work at all!
# Program no. 1 with the bug:


for x in range(3):
    print(x)

for j in range(5):
    print("This is a loop number ", j)

x = 10
while x > 0:
    print(x)
    x -= 1

f = 5
while f > 0:
    print(f)
    f -= 1
else:
    print("Start!")






# Task 5 - summing three integers
# Your task is to fix program non-working correctly. The problem:
#
# sum the three prompted integers
# however, if two values are equal sum should be zero
# calculate what result should be and what you get after running the program

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or x == z:
    print(0)
else:
    sum = x + y + z
    print("Calculated sum is ", sum)






# Task 6 - summing two integers
# Your task is to fix program non-working correctly. The problem:
#
# sum the two prompted integers
# however, if the sum is between 15 to 20 (both numbers included) it should be calculated to 20
# calculate what result should be and what you get after running the program
# Program with bugs:


x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y
if result > 15 and result < 20:
    print("Calculated sum is 20")
else:
    print(result)






# Task 7 - swapping variables
# Your task is to fix program non-working correctly. The problem:
#
# prompt two values and assign them to variables a and b
# write the Python program to swap these two variables
# calculate what result should be and what you get after running the program
# Remark: don't use "fast" swapping available in Python:


a = input("First value: ")
b = input("Second value: ")
print("Before swapping: a =", a, ", b =", b)

print("After swapping: a =", b, ", b =", a)





# Task 8 - max and min values
# Your task is to fix program non-working correctly. The problem:
#
# prompt three float numbers and determine the largest and the smallest one
# calculate what result should be and what you get after running the program

x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))







# Task 9 - convertion
# Your task is to fix program non-working correctly. The problem:
#
# prompt value from the user and assign it to some variable
# if given value is 0 (zero) convert it to False and if given value is 1 convert it to True
# display results


x = input("Type your value: ")
if x == "0":
    print('Your entered value is now False')
elif x == "1":
   print('Your entered value is now True')
else:
    print('Your entered value is now', x)







# Task 10 - divisible number
# Your task is to fix program non-working correctly. The problem:
#
# accept (prompt) two integers values from the user
# check whether a first number is divisible by second number and vice versa
# display results

x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by the second number, result = ", x / y)
elif y % x == 0:
    print("Second number is divisible by the first number, result = ", y / x)
else:
    print("Numbers are non-divisible!")
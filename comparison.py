# Comparison and logical operators
# In this exercise, we will focus on the usage of the comparison and logical operators, including:
#
# equal operator ==,
# not equal operator !=,
# greater than operator >,
# less than operator <,
# greater than or equal to operator >=,
# less than or equal to operator <=,
# and, or, not logical operators,
# using None.


# Task 1 - comparison operators
# Your task is to write a program which asks the user three times about two integer numbers to compare.
#
# Hint: Use while loop to perform the same operation more than once!
#
# Use both comparison and logical operators, for example use logical comparison between two or more comparison operators:
#





# using None.



x = 1
while x <= 3:
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))
    if num1 == num2: # equal operator ==,
        print(num1, 'is equal to ', num2)
    elif num1 > num2: # greater than operator >,
        print(num1, 'is greater than ', num2)
    else: # less than operator <,
        print(num1, 'is less than ', num2)

    if num1 != num2: # not equal operator !=,
        print(num1, 'is not equal to ', num2)
    elif num1 >= num2: # greater than or equal to operator >=,
        print(num1, 'is greater than or equal to ', num2)
    else: # less than or equal to operator <=,
        print(num1, 'is less than or equal to ', num2)

    if num1 > 1000 and num2 > 1000:
        print('Both numbers are great')
    elif num1 > 1000 or num2 > 1000:
        print('One of the numbers is big')
    elif not (int(num1) > 1000 and not int(num2) > 1000):
        print('The numbers are small')
    else:
        print('Everything is fine')
    x += 1

#Task 2 - convertion month name to a number of days
# Your task is to write a Python program to convert month name to a number of days.
#
# Hint: Print list of months at the beginning.
#
# User should be prompted to enter name of the month and the output should be the number of days in given month.
#
# Some of your results could look like this:
# List of months: January, February, March, April, May, June, July, August, September, October, November, December
# Input the name of Month: May
# Number of days: 31 days

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month = str(input("Input the name of Month: "))

if month == "February":
	print("Number of days: 28/29 days")
elif month in ("April", "June", "September", "November"):
	print("Number of days: 30 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
	print("Number of days: 31 day")
else:
	print("Wrong month name")





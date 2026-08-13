# Importing the math library lets you use squareroot(sqrt) and power(pow) functions later on to calculate the distance between two points.
import math

# This program requires you to input the value of (x1,y1) to calculate the distance between point 1 and point 2.
x1 = float(input("Enter value of x1: "))
y1 = float(input("Enter value of y1: "))

# This program requires you to input the value of (x2,y2) to calculate the distance between point 2 and point 1.
x2 = float(input("Enter value of x2: "))
y2 = float(input("Enter value of y2: "))

# This will calculate the distance between the two points using the distance formula. 
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

#  This will print the answer of the distance between the two points.
print("The distance between the two points is: ", distance)

# This is my reflection regarding why the use of libraries is more practical than writing all calculations from scratch.
    
"""
Using a library is more practical than writing all calculations from scratch because the math library provides tested functions.
Instead of using complex mathematical formulas for just one question, we can use the built-in functions to get the answer with less effort, less time and more accuracy.
"""

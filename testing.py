import math

x1 = float(input("Enter the first number: "))
x2 = float(input("Enter the second number: "))
y1 = float(input("Enter the third number: "))
y2 = float(input("Enter the fourth number: "))

# Calculate the distance between two points using the distance formula
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance:", d)

# Function for use: This script calculates the distance between two points (x1, y1) and (x2, y2) using the distance formula.

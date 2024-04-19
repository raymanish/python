# Function for use: This script calculates the average marks of four subjects and determines whether the student has passed or failed.
a = int(input("Enter the marks of 1st subject:"))
b = int(input("Enter the marks of 2nd subject:"))
c = int(input("Enter the marks of 3rd subject:"))
d = int(input("Enter the marks of 4th subject:"))

average_marks = (a + b + c + d) / 4

if average_marks >= 50:
    print("You have failed")
else:
    print("You have passed")

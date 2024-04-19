# Function for use: This script calculates the average score of two subjects and determines whether the average score indicates a pass or fail.
m1 = int(input("Enter the score for the 1st subject:"))
m2 = int(input("Enter the score for the 2nd subject:"))

total = m1 + m2
avg = total / 2

if avg >= 50:
    print("Pass")
else:
    print("Fail")

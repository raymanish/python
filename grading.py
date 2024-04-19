a= int(input("enter the marks of 1st subject:"))
b= int(input("enter the marks of 2nd subject:"))
c= int(input("enter the marks of 3rd subject:"))
d= int(input("enter the marks of 4th subject:"))

average_marks=(a+b+c+d/4)
if average_marks>=50:
    print("you have failed")
else:
    print("you have passed")
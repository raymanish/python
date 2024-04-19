student_id = input("Enter your student ID: ")
student_fn = input("Enter the first name of the student: ")
student_ln = input("Enter the last name of the student: ")
m = "I am a newbie in Whitecliffe College!"
w = m.split()
print("Split words:", w)
for g in w:
    if g.lower() == "whitecliffe" or g.lower() == "college":
        print(g)

# Function for use: This script prompts the user to enter student information and then splits a sentence into words. 
# It searches for specific words in the sentence (case-insensitive) and prints them if found.

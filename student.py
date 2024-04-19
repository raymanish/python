student_id = input("Enter the student id:")
student_fn = input("Enter the first name of the student:")
student_ln = input("Enter the last name of the student:")
message = "I am a newbie In Whitecliffe college !"
words = message.split()
print("words=", words)
for i in words:
        if i == "Whitecliffe" or i == "college":
            print(i)
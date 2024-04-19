import random

class Membership:
    status = "Active"

    def __init__(self):
        # Initialize instance variables
        self.student_id = ''
        self.stud_lastname = ''
        self.stud_program = ''
        self.mem_id = ''
        self.status = Membership.status

    def stud_data(self):
        # Collect student data
        self.student_id = input("Enter your Whitecliffe student Id: ")
        self.stud_lastname = input("Enter your last name: ")
        self.stud_program = input("Enter the name of your programme: ")

    def generate_mem_id(self):
        # Generate membership ID if student ID is registered
        registered_stud = ['S1', 'S2', 'S3', 'S4', 'S5']
        if self.student_id in registered_stud:
            g_mem_id = random.randint(1, 10)
            return g_mem_id

    def display(self):
        # Display student information
        print("Membership ID:", self.mem_id)
        print("Student ID:", self.student_id)
        print("Last Name:", self.stud_lastname)
        print("Programme:", self.stud_program)
        print("Status:", self.status)

    def withdrawal(self, ln):
        # Withdraw student based on last name
        if self.stud_lastname == ln:
            self.status = "Withdrawn"

# List to store registered students
registration = []

# Register students
num = int(input("How many students are you registering today?"))
for i in range(num):
    member = Membership()
    member.stud_data()
    member.display()
    member.withdrawal("manish")  # Withdraw based on last name "Guru"
    registration.append(member)

# Withdraw a specific student
name = input("Enter the name of the student withdrawing: ")
for i in range(num):
    registration[i].withdrawal(name)
    registration[i].display()

# Count the number of active, withdrawn, diploma, and degree students
active = 0
withdrawn = 0
diploma = 0
degree = 0
for i in range(num):
    if registration[i].status == "Active":
        active += 1
    if registration[i].status == "Withdrawn":
        withdrawn += 1
    if registration[i].stud_program.lower() == "diploma":
        diploma += 1
    if registration[i].stud_program.lower() == "degree":
        degree += 1

# Print statistics
print("The number of active members:", active)
print("The number of withdrawn students:", withdrawn)
print("The number of diploma students:", diploma)
print("The number of degree students:", degree)

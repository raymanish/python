import random
class Membership:
    status="Active"
    def _init_(self):
        self.student_id= ''
        self.stud_lastname= ''
        self.stud_program= ''
        self.mem_id= ''
        self.status= Membership.status
    def stud_data(self):
        self.student_id= input("Enter your Whitecliffe student Id: ")
        self.stud_lastname= input("Enter your last name: ")
        self.stud_program= input("Enter the name of your programme: ")

    def generate_mem_id(self):
        registered_stud= ['S1', 'S2', 'S3', 'S4', 'S5']
        if self.student_id in registered_stud:
            g_mem_id= random.randint(1,10)
            return g_mem_id
    def display(self):
        print(self.mem_id)
        print(self.student_id)
        print(self.stud_lastname)
        print(self.stud_program)
        print(self.status)

    def withdrawal(self,ln):
        if self.stud_lastname == ln:
            self.status = "withdrawn"
registration=[]
num= int(input("How many students you are registering today?"))
for i in range(num):
    k= Membership()
    k.stud_data()
    k.display()
    k.withdrawal("Guru")
    registration.append(k)
    #print(k.generate_mem_id())

name=input("Enter the name of the student withdrawing")
for i in range(num):
    registration[i].withdrawal(name)
    registration[i].display()

active=0
withdrawn=0
diploma=0
degree=0
for i in range(num):
    if registration[i].status== "Active":
        active+= 1
    if registration[i].status=="withdrawn":
        withdrawn+=1
    if registration[i].stud_program=="diploma":
        diploma+=1
    if registration[i].stud_program=="degree":
        degree+=1
print("The number of active members:", active)
print("The number of withdrawn students: ", withdrawn)
print("The number of diploma students: ", diploma)
print("The number of degree students:", degree)


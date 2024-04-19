def check_students_status(*marks):
    # calculate the total marks by summing up all the marks
    total_marks =sum(marks)
    # calculate the number of subjects by counting the number of marks provided
    num_subjects =len(marks)
    # calculate the average marks by dividing the total marks by the number of subjects
    average_marks =total_marks /num_subjects
    # check if average marks are greater than or equal to the passing values
    passing_values = 50 # assuming passing values is 50
    if average_marks >= passing_values:
        return "passed"
    else:
         return "failed"

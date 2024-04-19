class GradingSystem:
    def __init__(self):
        # Initialize instance attributes
        self.average = self.Average()
        self.classification = ''

    def average(self):
        # Input the number of subjects
        num = int(input("Enter the number of subjects:"))
        arr_score = []
        # Input scores for each subject
        for i in range(num):
            input_score = int(input("Enter the score:"))
            arr_score.append(input_score)
        sum = 0
        # Calculate the sum of scores
        for score in arr_score:
            sum += score
        # Calculate the average score
        average = sum / len(arr_score)
        return average

    # Example usage
    grading_system = GradingSystem()
    print("Average score:", grading_system.average)

# Comment for the function: This class calculates the average score of subjects.

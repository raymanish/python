class GradingSystem:
    def average(self):
        # Input the number of subjects
        num = int(input("Enter the number of subjects:"))
        arr_scores = []
        # Input scores for each subject
        for i in range(num):
            input_score = int(input("Enter score:"))
            arr_scores.append(input_score)
        sum = 0
        # Calculate the sum of scores
        for i in arr_scores:
            sum = sum + i
        # Calculate the average score
        average = sum / len(arr_scores)
        print(average)
        return average

    def grading(self):
        # Calculate the average score
        av = self.average()
        # Assign grades based on the average score
        if av > 90:
            print("First Class")
        elif av >= 70:
            print("Second Class Upper")
        elif av >= 60:
            print("Second Lower Class")
        elif 50 <= av < 60:
            print("Pass")
        else:
            print("Fail")

# Example usage
grading_system = GradingSystem()
grading_system.grading()

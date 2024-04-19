class GradingSystem:

    def average(self):
        num=int(input("Enter the number of subjects:"))
        arr_scores=[]
        for i in range(num):
            input_score=int(input("Enter score:"))
            arr_scores.append(input_score)
        sum=0
        for i in arr_scores:
            sum=sum+i
        average=sum/len(arr_scores)
        print (average)
        return average
    def grading(self):
        av=self.average()
        if av > 90:
            print("FirstClass")
        elif av >= 70:
            print("Second class upper")
        elif av >= 60:
            print("Second lower class")
        elif av <60 and av >=50:
            print("pass")
        elif av < 50:
            print("Fail")


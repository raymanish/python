class GradingSystem:

    def __init__(self):

        self.average= GradingSystem.Average()
        self.classification=''

    def average(self):
        num=int(input("enter the number of subject"))
        arr_score=[]
        for i in range(num):
            input_score=int(input("enter the score"))
            arr_score.append(input_score)
            sum=0
            for i in arr_score:
                sum=sum+i
                average=sum/len(arr_score)

                return average
            



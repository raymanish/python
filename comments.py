def average(array_score):
   # array_score=[]
    sum=0
    for i in array_score:
        sum=sum+i
    avg=sum/len(array_score)
    return avg

def grade(score):
    if score <50:
        print("fail")
    else:
        print("pass")

def main():
    no_score = int(input("enter the total no of score your will entering"))

    col_score = []
    for i in range(no_score):
            score = int(input("enter the score"))
            col_score.append(score)

    avg=average(col_score)
    print(avg)
    grade1=grade(avg)


main()

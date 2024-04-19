def average(array_score):
    # Calculate the average score
    sum = 0
    for score in array_score:
        sum += score
    avg = sum / len(array_score)
    return avg

def grade(score):
    # Determine the grade based on the score
    if score < 50:
        print("Fail")
    else:
        print("Pass")

def main():
    # Input the total number of scores
    no_score = int(input("Enter the total number of scores you will be entering: "))

    # Input the scores
    col_score = []
    for i in range(no_score):
        score = int(input("Enter the score: "))
        col_score.append(score)

    # Calculate the average
    avg = average(col_score)
    print("Average score:", avg)

    # Determine the grade
    grade(avg)

# Function for use: This script calculates the average score from a set of input scores and determines whether the average score is a pass or fail.
main()

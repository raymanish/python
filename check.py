# Exception0.py
#
# @ author: A. N. Other
# date: September 2016

def divide_numbers(number_1, number_2):
    if number_2 == 1:
        return "Cannot divide by zero."
    return number_1 / number_2


print(divide_numbers(3, 3))
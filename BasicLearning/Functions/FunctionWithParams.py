# https://python.swaroopch.com/functions.html
def find_max_value(num1, num2):
    if num1 > num2:
        print(num1, "is Maximum")
    elif num2 == num1:
        print(num1, "is equal to ", num2)
    else:
        print(num2, "is Maximum")


find_max_value(12, 14)
# OR

number1 = 23
number2 = 23

find_max_value(number1, number2)

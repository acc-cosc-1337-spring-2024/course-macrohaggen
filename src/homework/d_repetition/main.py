from repetition import get_factorial
from repetition import sum_odd_numbers
choice = " "
while choice != "yes" or choice != "y":
    print("Homework 3 Menu\n","1 - Factorial\n", "2 - Sum Odd Numbers\n","3 - Exit\n")
    decNum = int(input(""))
    if decNum == 1:
        facNum = int(input("Enter Number: \n"))
        print(get_factorial(facNum))
        print("Do you want to exit? (y/n)\n")
        choice == input("")
    elif decNum == 2:
        sumNum = int(input("Enter Number: \n"))
        print(sum_odd_numbers(sumNum))
        print("Do you want to exit? (y/n)\n")
        choice == input("")

    elif decNum == 3:
        print("Do you want to exit? (y/n)\n")
        choice == input("")
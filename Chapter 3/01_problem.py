"""
1. Number Analyser
Write a program that asks the user to enter an integer. The program should display
“Positive” if the number is greater than 0, “Negative” if the number is less than 0, and
“Zero” if the number is equal to 0. The program should then display “Even” if the number
is even, and “Odd” if the number is odd.

*****************************************
ask from user to enter a number
check if the number is positive, negative or zero
check if the number is even or odd


"""

while True:
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positve")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


    user_input = input("Do you want to continue? (y/n): ")
    if user_input   == 'y':
        continue
    else:
        break

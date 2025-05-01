''''7. Stadium Seating
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
$15, and Class C seats cost $10. Write a program that asks how many tickets for each class
of seats were sold, then displays the amount of income generated from ticket sales.'''

print('There are three types of tickets')
print("Class A = $20")
print("Class B = $15")
print("Class C = $10")

a = 1    
b = 2 
c = 3 
total_A = 0 
total_B = 0
total_C = 0
keep_going = "y" or "Y"
while keep_going == "y" or keep_going=="Y":
    
    choice = input("Which class ticket you want to buy: ")

    if choice == "a":
        total_A += 1
        # print(f"Total number of Class A ticeke are sold: {total_A}")
    elif choice == "b":
        total_B += 1
        # print(f"Total number of Class B ticeke are sold: {total_B}")
    elif choice == 'c':
        total_C += 1
        # print(f"Total number of Class C ticeke are sold: {total_A}")
    else:
        print("Invalid Entery")
    

    


    keep_going = input("you want to buy more ticket(Y for continue, N for exit): ")
    # input(keep_going)
    print()
print(f"Total number of Class A ticeke are sold: {total_A}")
print(f"Total number of Class B ticeke are sold: {total_B}")
print(f"Total number of Class C ticeke are sold: {total_C}")
print(f"Total Number ticket are sold:{total_A + total_B + total_C} ")

print(f"Totla income from Class A {total_A * 20}")
print(f"Totla income from Class B {total_B * 15}")
print(f"Totla income from Class A {total_C * 10}")

# def display_menu():
#     print('There are three types of tickrts')
#     print("Class A = $20")
#     print("Class B = $15")
#     print("Class C = $10")
    


# def no_of_tickets():
#     print("Total number of tickets sold")
#     while True:
#         choice = str(input('Which class ticket you want to buy: '))
#         A=1
#         B=2
#         C=3
#         for i in range():
#             if choice == 1:
#                 A += 1
#                 print(f"you are buy the Class A ticket {A} ")
#             elif choice == 2:
#                 B += 1
#                 print("you are buy the Class B ticket ")
#             elif choice == 3:
#                 C += 1
#                 print("you are buy the Class C ticket ")
#             else:
#                 print('Invalid choice')
#                 break
#             total = A + B + C
#             return A, B, C, total
#         input('Do you want to buy more tickets? (y/n): ')

# def calculate_income(A, B, C):
#     total = A * 20 + B * 15 + C * 10
#     return total

# def main():
#     display_menu()
    
#     no_of_tickets() #ticket sold
#     A, B, C = no_of_tickets()
#     total = calculate_income(A, B, C)
#     print('The total income generated from ticket sales is: $', total)

# main()
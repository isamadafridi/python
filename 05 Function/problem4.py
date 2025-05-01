'''4. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.'''

def monthaly_cost():
    loan_payment = float(input("Enter the loan payment: "))
    insurance = float(input("Enter the insurance: "))
    gas = float(input("Enter the gas: "))
    oil = float(input("Enter the oil: "))
    tires = float(input("Enter the tires: "))
    maintenance = float(input("Enter the maintenance: "))
    total_monthaly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    print("The total monthaly cost is: ", total_monthaly_cost)
    total_annual_cost = total_monthaly_cost * 12 
    print("The total annual cost is: ", total_annual_cost)

def main():
    monthaly_cost()

main()
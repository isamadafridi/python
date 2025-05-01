'''8. Paint Job Estimator
A painting company has determined that for every 112 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $35.00 per hour
for labor. Write a program that asks the user to enter the square feet of wall space to be
painted and the price of the paint per gallon. The program should display the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job.
________________________________________________

'''
import math

def calculate_gallon(wall_space):
    return math.ceil(wall_space / cover_per_gallon)

def calculte_labor_hours(gallon_req):
    return gallon_req * hour_per_gallon

def calculate_cost_paint(gallon_req, gallon_price):
    return gallon_req* gallon_price

def calculate_labor_charge(labour_hours_req):
    return labor_per_hour * labour_hours_req

def calculate_total_cost(paint_cost, labor_charge):
    return paint_cost + labor_charge

cover_per_gallon = 112
hour_per_gallon = 8
labor_per_hour = 35.00

def main():
    wall_space = float(input('Enter the sqaure feet of the wall: '))
    gallon_price = float(input('Enetr the price per gallon: '))

    gallon_req = calculate_gallon(wall_space) #Call the to show gallon required
    labor_hours_req = calculte_labor_hours(gallon_req)
    paint_cost = calculate_cost_paint(gallon_req , gallon_price)
    labor_charge = calculate_labor_charge(labor_hours_req)
    total_paint_cost = calculate_total_cost(paint_cost , labor_charge)

    print(f"---Paint Job Estimate---")
    print(f"The number of gallons of paint required: {gallon_req}")
    print(f"The hours of labor required: {labor_hours_req}")
    print(f"The cost of the paint: {paint_cost}")
    print(f"The labor charges: {labor_charge}")
    print(f"The total cost of the paint job: {total_paint_cost}")

  
main()

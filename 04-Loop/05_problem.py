'''5. Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall over
a period of years. The program should first ask for the number of years. The outer loop will
iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.'''

year = int(input("Enter the NUmber of years: "))
total_rainfall=0
total_months = 0
average_ranifall = 0
for y in range(1,year+1):
    for m in range(1, 12+1):
        rainfall = int(input(f"Enter the {m} months of the year {y} rainfall in inches: "))
        total_months += 1
        # print("totla months",total_months)
        total_rainfall += rainfall
average_ranifall= (total_rainfall / total_months)
print(f'The total number of months are \'\"{total_months}\" , the total inches of rainfall \"{total_rainfall}\" , the average rainfall per month for the entire period are \"{average_ranifall}\".')



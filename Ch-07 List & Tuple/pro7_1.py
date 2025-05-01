Num_days=int(input("How many days of sales you want to enter?: "))
def main():

    

    sales = [0] * Num_days
    index = 0
    while index < len(sales):
        sales[index] = float(input(f"Enter the sales for day {index + 1}:  "))
        index += 1
    print(sales)


main()


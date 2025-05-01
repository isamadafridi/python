#Constent value
mile = 0.6214

# Kilo to mile conversion function
def kilo_to_mile(km):
    miles = km * mile
    print(f"The distance in miles is: {miles:.2f}")
    # return km * mile

# Main function
def main():
    km = float(input("Enter the distance in kilometers: "))
    kilo_to_mile(km)

main()
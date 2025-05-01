'''Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
program that calculates the number of packages of hot dogs and the number of packages of
hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
should ask the user for the number of people attending the cookout and the number of hot
dogs each person will be given. The program should display the following details:
• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over
************************************************************
Ask from user to enter the number of people attending the cookout
Ask from user to enter the number of hot dogs each person will be given
Calculate the minimum number of packages of hot dogs required
Calculate the minimum number of packages of hot dog buns required
Calculate the number of hot dogs that will be left over
Calculate the number of hot dog buns that will be left over
Display the minimum number of packages of hot dogs required
Display the minimum number of packages of hot dog buns required
Display the number of hot dogs that will be left over
Display the number of hot dog buns that will be left over

'''
import math

# Get input from user
people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Calculate total number of hot dogs needed
total_hot_dogs = people * hot_dogs_per_person

# Constants for package sizes
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Calculate the number of packages required
hot_dog_packages = math.ceil(total_hot_dogs / HOT_DOGS_PER_PACKAGE)
bun_packages = math.ceil(total_hot_dogs / BUNS_PER_PACKAGE)

# Calculate leftovers
hot_dogs_leftover = (hot_dog_packages * HOT_DOGS_PER_PACKAGE) - total_hot_dogs
buns_leftover = (bun_packages * BUNS_PER_PACKAGE) - total_hot_dogs

# Display the results
print("\n--- Cookout Summary ---")
print(f"Minimum number of hot dog packages required: {hot_dog_packages}")
print(f"Minimum number of hot dog bun packages required: {bun_packages}")
print(f"Number of hot dogs left over: {hot_dogs_leftover}")
print(f"Number of hot dog buns left over: {buns_leftover}")






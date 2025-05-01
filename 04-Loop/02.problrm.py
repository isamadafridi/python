'''2. Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.





'''
cpm = 4.2
for i in range(10, 30+5, 5):
    num_of_cal = cpm * i
    print(f"Number of Callories after {i} minutes", num_of_cal)





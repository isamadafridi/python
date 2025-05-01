'''1. Bug Collector
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when

pseduo code
1. Initialize the accumulator.
2. For each of the five days
    a. Input the number of bugs collected for a day
    b. Add the number of bugs to the accumulator
3. Display the total bugs collected
'''

bug = 0
days= 5
total_bugs = 0
for i in range(days):
    bug = int(input("Enter the number of bugs collected for the day: "))
    total_bugs = total_bugs + bug
print(F"The total number of bugs collected for the {days} days is:  {total_bugs}")

'''6. Miles to Kilometers Table
Write a program that displays a table of distances in miles and their equivalent distances in
kilometers, rounded to 2 decimal places. One mile is equivalent to 1.60934 kilometers. The
table should be generated using a loop, and should include values in 10 mile increments from
10 to 80.'''


miles = 1.60934
print(f"Miles \t KM")
print("------------")
for i in range(10, 80+10, 10):
    km = i* miles
    print(f"{i} \t {format(km,'.2f')}")
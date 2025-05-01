"""2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectangle
has the greater area, or if the areas are the same.

************************************************************
Ask from user to enter the length and width of two rectangles
Calculate the area of two rectangles
Compare the area of two rectangles
Display the result

"""


lenth1 = int(input("Enetr the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

area1 = lenth1 * width1
print("Area of rectangle 1 is: ", area1)

lenth2 = int(input("Enetr the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

area2 = lenth2 * width2
print("Area of rectangle 2 is: ", area2)

if area1 > area2:
    print("Area of rectangle 1 is greater than rectangle 2")
else:
    print("Area of rectangle 2 is greater than rectangle 1")
    


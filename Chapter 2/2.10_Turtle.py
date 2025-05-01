# import turtle
# turtle.showturtle()
# turtle.forward(100)
# # turtle.right(90)
# # turtle.forward(100)
# # turtle.right(90)
# # turtle.forward(100)
# # turtle.right(90)
# # turtle.forward(100)
# # turtle.right(90)
# turtle.done()
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Dark background
screen.title("Colorful Turtle Spiral")

# Create a turtle
spiral = turtle.Turtle()
spiral.speed(100)  # Fastest animation speed
spiral.width(2)

# Create color transition
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the spiral pattern
for i in range(200):
    spiral.pencolor(colors[i % 6])  # Cycle through colors
    spiral.forward(i * 1.5)
    spiral.left(59)  # Creates an interesting angle pattern

# Add background decoration
decoration = turtle.Turtle()
decoration.speed(0)
decoration.hideturtle()

# Draw circular background elements
for i in range(36):
    decoration.color("cyan")
    decoration.circle(150)
    decoration.left(10)

# Hide the turtle and finish
spiral.hideturtle()
turtle.done()
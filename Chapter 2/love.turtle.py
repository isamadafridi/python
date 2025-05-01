import turtle

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")

heart = turtle.Turtle()
heart.speed(10)  # Fastest animation speed
heart.color("red")
heart.pensize(2)

# Start filling color
heart.begin_fill()

# Draw the heart shape
heart.left(140)
heart.forward(113)
for _ in range(200):
    heart.right(1)
    heart.forward(1)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(1)
heart.forward(112)

# Complete the fill and hide turtle
heart.end_fill()
heart.hideturtle()

# Keep window open
turtle.done()
import turtle

# Set up the screen
screen = turtle.Screen()
t = turtle.Turtle()

screen.title("My Turtle Art")
screen.bgcolor("")  # Set background color
screen.setup(width=800, height=600)  # Window size

# for i in range(5):
#     t.forward(100)
#     t.right(144)



t.color("black", "blue")
t.begin_fill()
t.circle(100)
t.end_fill()


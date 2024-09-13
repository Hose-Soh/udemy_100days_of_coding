from turtle import *

mini = Turtle("turtle")
mini.color("green")

screen = Screen()

for i in range(4):
    mini.speed("slowest")
    mini.forward(100)
    if i <3:
        mini.right(90)

# screen.exitonclick()


# mini = Turtle("turtle")
# mini.color("green")

# screen = Screen()
for _ in range(10):
    mini.speed("slowest")
    mini.forward(10)
    mini.penup()
    mini.forward(10)
    mini.pendown()


screen.exitonclick()

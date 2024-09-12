import turtle
from turtle import Screen

mini = turtle.Turtle()
print(mini)
mini.shape("turtle")
mini.color("green")
mini.forward(100)
mini.speed("slowest")

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

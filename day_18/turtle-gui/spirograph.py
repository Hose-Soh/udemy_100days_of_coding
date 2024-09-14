from email.policy import default
from turtle import Turtle, Screen
import random
from draw_shape import COLOR

spiro = Turtle()
spiro_screen = Screen()
spiro.speed("fastest")
spiro_screen.colormode(255)

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        spiro.pencolor(rand_color())
        spiro.circle(80)
        spiro.right(gap_size)

spirograph(3)

spiro_screen.exitonclick()

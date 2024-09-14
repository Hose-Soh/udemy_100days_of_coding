from random import randrange
from turtle import Turtle, Screen
from draw_shape import DrawShape, COLOR

import random

mini = Turtle("turtle")
mini.color("green")

screen = Screen()
screen.bgcolor("DarkSlateGray3")

# Define boundaries for movement
def move(steps, turtle_obj):
    # Compute new position based on heading
    turtle_obj.forward(steps)
    new_x, new_y = turtle_obj.pos()

    # If out of bounds, undo movement
    if not (-300 < new_x < 300 and -300 < new_y < 300):
        turtle_obj.back(steps)

def rand_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

total_steps = 0
mini.pensize(10)
mini.speed("fastest")
screen.colormode(255)

while total_steps <1000:
    mini.pencolor(rand_color())
    move(random.randrange(15, 20), mini)
    if random.choice([True, False]):
        mini.right(random.choice([0, 90]))
    else:
        mini.left(random.choice([0, 90]))

    total_steps+=1


screen.exitonclick()

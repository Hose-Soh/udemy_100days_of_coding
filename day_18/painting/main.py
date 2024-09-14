# import colorgram
import random
from turtle import Turtle, Screen

# colors = colorgram.extract("image.jpg", 50)
# #(type(colors))
# #print(colors)
#
# rgb_list = []
#
# for i in range(len(colors)):
#     rgb_list.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
#
# print(rgb_list)

rgb_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
            (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
            (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (58, 12, 25),
            (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52), (252, 7, 40),
            (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8)]

# define new turtle object and screen object
dot = Turtle()
dot_screen = Screen()

dot.speed("fastest")

# set initial position
dot.up()
dot.setpos(-250, -250)
dot.down()

# set color mode to 255 so that screen can process rgb_list
dot_screen.colormode(255)

# run loop for 10 by 10 dot painting

for row in range(1, 11):
    for col in range(1, 11):
        dot.dot(20, random.choice(rgb_list))
        if col<10:
            dot.up()
            dot.forward(50)
            dot.down()
    if row <10:
        dot.up()
        dot.setpos(-250, -250+(row*50))
        dot.down()

dot_screen.exitonclick()
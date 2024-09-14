from turtle import Turtle, Screen
from draw_shape import DrawShape

mini = Turtle("turtle")
mini.color("green")

screen = Screen()


# # draw rectangle
# for i in range(4):
# #    mini.speed("slowest")
#     mini.pencolor("black")
#     mini.forward(100)
#     if i <3:
#         mini.right(90)
#
# # screen.exitonclick()
#
#
# # mini = Turtle("turtle")
# # mini.color("green")
#
# # draw dashed line
# # screen = Screen()
# for _ in range(8):
# #    mini.speed("slowest")
#     mini.pencolor("gray")
#     mini.forward(10)
#     mini.penup()
#     mini.forward(10)
#     mini.pendown()

mini.penup()
mini.sety(90)
mini.setx(35)
mini.pendown()


triangle = DrawShape(mini, 3)
square = DrawShape(mini, 4)
pen = DrawShape(mini, 5)
hexa = DrawShape(mini, 6)
hep = DrawShape(mini, 7)
octa = DrawShape(mini, 8)
non = DrawShape(mini, 9)
dec = DrawShape(mini, 10)

screen.exitonclick()
